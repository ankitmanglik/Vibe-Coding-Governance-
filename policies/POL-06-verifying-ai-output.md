# POL-06 Verifying AI output

**Purpose:** Treat AI output as a confident first draft, not a finished product.

**Plain-English background:** AI tools can sound certain while being wrong. In the incident log an AI faked data, claimed a rollback was impossible when a backup existed *(VC-01)*, and said there were "no issues" in code that was sending thousands of emails *(VC-28)*.

## VO-1 Small changes, one at a time

- Ask for one change at a time. Check it works. Save (commit). Then ask for the next. *(VC-02, VC-05, VC-06, VC-30)*
- Avoid "rewrite the whole thing" requests on working projects; they cause "state drift", where unrelated parts quietly break. *(VC-30)*
- Look at what changed (the "diff") before accepting. If you can't read it, at least check *which files* changed and whether that makes sense.

## VO-2 Verify claims yourself

- When the AI says something is "fixed", "safe", "tested", or "impossible", check it yourself or ask someone else. *(VC-01, VC-28)*
- Ask the AI to show evidence: "Show me the test you ran and its output", "Show me where the backup is."

## VO-3 Describe what "working" means, then check it

- Before building, write in plain words what should happen, including what should *not* happen (for example, "a logged-out visitor cannot see the orders page"). *(VC-29)*
- After each change, check those statements by hand or with tests.

## VO-4 Keep rules in a project file, and restart long sessions

- Put your project's rules in a file the AI reads every session (for Claude Code, `CLAUDE.md`). Rules typed only in chat can be lost when the AI summarizes a long conversation. *(VC-10)*
- For long tasks, start a fresh session with a short summary rather than running one session for hours.

## VO-5 Know when to bring in an engineer

Stop and ask for technical help when:
- the same bug comes back after three attempts,
- the AI is "fixing" one thing and breaking another,
- the project now handles money, personal data, or many users,
- you don't understand what a change does. *(VC-06, VC-29)*

## VO-6 Check packages before installing

- AI sometimes suggests software packages that don't exist, or look-alike fakes. Before installing, check the package's official page: is it real, widely used, and recently maintained? *(VC-05)*
