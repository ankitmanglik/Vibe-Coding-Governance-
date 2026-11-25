# Guardrails (enforcement)

Policies say what should happen; guardrails make the AI tool enforce it. This folder currently covers **Claude Code**. Contributions for other tools are welcome.

| File | What it does | Controls |
|---|---|---|
| `claude-code/settings.json` | Project settings: blocks the AI from reading secret files, and makes it ask before risky commands. | AS-1, EB-4, VO-6 |
| `claude-code/hooks/vibe_guard.py` | A small Python 3.14 safety check that runs before every command or file write. It asks you first for destructive commands and secrets in code, and refuses drive-wiping commands. | EB-4, EB-6, AS-1, AS-3, CL-3 |
| `claude-code/managed-settings.example.json` | Organization-wide version for IT admins. It also switches off "bypass permissions" mode so users can't turn the guardrails off. | RT-3, EB-4, EB-6 |
| `claude-code/CLAUDE.md.template` | Project rules file that Claude reads every session, so the rules survive long chats. | VO-4 |

## Install for one project (builders)

1. Make sure Python 3.14 is installed (`python3 --version`).
2. In your project folder, create a `.claude` folder with a `hooks` folder inside it.
3. Copy `settings.json` to `.claude/settings.json`.
4. Copy `hooks/vibe_guard.py` to `.claude/hooks/vibe_guard.py`.
5. Copy `CLAUDE.md.template` to `CLAUDE.md` in the project folder and fill it in.
6. On Windows, change `python3` to `python` in `settings.json` if `python3` isn't recognised.

## Install for the whole organization (IT admins)

1. Place `vibe_guard.py` at a fixed path on each machine (the example uses `/opt/vibe-governance/vibe_guard.py`).
2. Deploy `managed-settings.example.json` as Claude Code's managed settings file, with the path adjusted. See Anthropic's Claude Code documentation on managed settings for its location on each operating system.
3. Managed settings take priority over user and project settings, so builders cannot switch them off.

## Limits

- Pattern matching is a safety net, not a guarantee. A determined or unusual command can slip past. Keep backups (EB-3) and least-privilege keys (AS-2); they protect you even when guardrails miss.
- The hook has not yet been tested. Try it in a sandbox project before rolling it out.
