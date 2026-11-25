#!/usr/bin/env python3
"""vibe_guard: a safety check that runs before Claude Code uses a tool.

What it does, in plain words:
  Claude Code calls this script just before it runs a command or writes a file.
  The script looks for dangerous patterns, for example "delete everything",
  "destroy the cloud setup", or "write a secret key into the code".
  If it finds one, it tells Claude Code to stop and ask you first
  (or, for the very worst cases, to refuse outright).

Why: see the toolkit's incidents/TRACEABILITY.md, controls EB-4, AS-1, AS-3.
Requires: Python 3.14. Uses only the standard library.

How Claude Code talks to this script:
  - It sends details of the tool call as JSON on standard input.
  - We reply with JSON on standard output saying "ask" or "deny",
    or print nothing to let the action go ahead normally.
"""

import json
import re
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Rule:
    """One dangerous pattern, and what to do when we see it."""

    pattern: str  # a regular expression (a text-matching pattern)
    decision: str  # "ask" = a person must approve; "deny" = never allowed
    reason: str  # shown to you and to Claude, in plain words


# Commands so dangerous they are never allowed (e.g. wiping a whole drive). (VC-09)
DENY_COMMANDS = [
    Rule(r"\brm\s+-[a-zA-Z]*[rR][a-zA-Z]*\s+(-[a-zA-Z]+\s+)*(/|~|\$HOME|[A-Za-z]:\\?)(\s|$|\*)",
         "deny", "Deleting your whole drive or home folder is never allowed."),
    Rule(r"\b(mkfs|format\s+[A-Za-z]:)", "deny", "Formatting a drive is never allowed."),
    Rule(r"\bdd\s+.*\bof=/dev/", "deny", "Writing directly to a disk is never allowed."),
]

# Commands that need a person to say yes first. (EB-4, EB-6, CL-3)
ASK_COMMANDS = [
    # Deleting or overwriting files (VC-02, VC-14)
    Rule(r"\brm\s+-[a-zA-Z]*[rRf]", "ask", "This deletes files, possibly many at once."),
    Rule(r"\bfind\b.*\s-(delete|exec\s+rm)\b", "ask", "This finds and deletes files in bulk."),
    Rule(r"\b(rmdir|rd|del|erase)\s+/[sq]", "ask", "This deletes folders on Windows."),
    Rule(r"Remove-Item\b.*-Recurse", "ask", "This deletes folders on Windows."),
    Rule(r"\b(mv|move|Move-Item)\b.*[*?]", "ask",
         "This moves many files at once. Check the destination folder exists first."),
    # Git history (VC-02)
    Rule(r"\bgit\s+reset\s+--hard\b", "ask", "This throws away all unsaved changes."),
    Rule(r"\bgit\s+clean\s+-[a-zA-Z]*f", "ask", "This deletes files Git isn't tracking."),
    Rule(r"\bgit\s+push\b.*(--force|-f\b|--mirror)", "ask", "This can overwrite the online copy's history."),
    Rule(r"\bgit\s+(checkout|restore)\s+(--\s+)?\.(\s|$)", "ask", "This throws away changes to every file."),
    Rule(r"\bgit\s+branch\s+-D\b", "ask", "This deletes a branch even if its work isn't saved elsewhere."),
    # Databases (VC-01, VC-08, VC-18)
    Rule(r"\b(drop|truncate)\s+(table|database|schema)\b", "ask", "This permanently deletes database data."),
    Rule(r"\bdelete\s+from\b", "ask", "This deletes rows from a database."),
    Rule(r"\b(supabase\s+db\s+reset|prisma\s+migrate\s+reset|--force-reset|rails\s+db:(drop|reset))",
         "ask", "This wipes and recreates a database."),
    Rule(r"\balter\s+table\b.*\bdisable\s+row\s+level\s+security\b", "ask",
         "This turns off the rule that keeps each user's data private."),
    # Infrastructure and cloud (VC-07, VC-08, VC-12)
    Rule(r"\b(terraform|tofu)\s+(destroy|apply)\b", "ask",
         "This changes or destroys cloud infrastructure. Only a technical owner should run it."),
    Rule(r"\bpulumi\s+(destroy|up)\b", "ask", "This changes or destroys cloud infrastructure."),
    Rule(r"\bkubectl\s+delete\b", "ask", "This deletes running cloud services."),
    Rule(r"\b(aws|gcloud|az|doctl|flyctl|railway|heroku|vercel|netlify)\b.*\b(delete|destroy|remove|rm|terminate|rb)\b",
         "ask", "This deletes something in a cloud account."),
    # Running code downloaded from the internet (VC-05)
    Rule(r"\b(curl|wget|iwr|Invoke-WebRequest)\b.*\|\s*(sh|bash|zsh|python3?|iex|powershell)\b", "ask",
         "This downloads and runs code from the internet in one step."),
    # Permissions
    Rule(r"\bchmod\s+(-R\s+)?777\b", "ask", "This lets anyone read and change these files."),
]

# Patterns that look like real secret keys. (AS-1, AS-3; VC-13, VC-15, VC-21)
SECRET_PATTERNS = [
    r"sk-(proj-|ant-)?[A-Za-z0-9_\-]{20,}",  # OpenAI / Anthropic style
    r"sk_live_[A-Za-z0-9]{16,}",  # Stripe live key
    r"AKIA[0-9A-Z]{16}",  # AWS access key
    r"gh[pousr]_[A-Za-z0-9]{30,}",  # GitHub token
    r"xox[abpr]-[A-Za-z0-9\-]{10,}",  # Slack token
    r"AIza[0-9A-Za-z_\-]{35}",  # Google API key
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",  # private key file
    r"service_role[\"']?\s*[:=]\s*[\"']eyJ",  # Supabase service-role key
]

# Files where secrets are SUPPOSED to live, so we don't warn about them.
SECRET_FILES = re.compile(r"(^|[/\\])\.env(\.[\w-]+)?$")


def check_command(command: str) -> Rule | None:
    """Return the first matching rule for a shell command, or None if it looks safe."""
    for rule in DENY_COMMANDS + ASK_COMMANDS:
        if re.search(rule.pattern, command, flags=re.IGNORECASE):
            return rule
    return None


def check_file_content(file_path: str, content: str) -> Rule | None:
    """Warn if a secret key is about to be written into a normal file."""
    if SECRET_FILES.search(file_path or ""):
        return None
    for pattern in SECRET_PATTERNS:
        if re.search(pattern, content or ""):
            return Rule(pattern, "ask",
                        "This looks like a secret key being written into a file. "
                        "Keys belong in the secret settings or a .env file, never in code.")
    return None


def text_being_written(tool_input: dict) -> str:
    """Collect the new text from Write, Edit, and MultiEdit tool calls."""
    parts = [tool_input.get("content", ""), tool_input.get("new_string", "")]
    parts += [edit.get("new_string", "") for edit in tool_input.get("edits", [])]
    return "\n".join(p for p in parts if p)


def main() -> None:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return  # Not something we understand: let Claude Code's normal rules apply.

    tool_input = event.get("tool_input", {}) or {}

    match event.get("tool_name"):
        case "Bash" | "PowerShell":
            rule = check_command(tool_input.get("command", ""))
        case "Write" | "Edit" | "MultiEdit":
            rule = check_file_content(tool_input.get("file_path", ""), text_being_written(tool_input))
        case _:
            rule = None

    if rule is None:
        return  # Looks fine: print nothing, so Claude Code carries on as usual.

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": rule.decision,
            "permissionDecisionReason": f"[vibe_guard] {rule.reason}",
        }
    }))


if __name__ == "__main__":
    main()
