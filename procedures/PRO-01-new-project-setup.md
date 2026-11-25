# PRO-01 New project setup

**When:** Before the first prompt of any new project above Tier 0.
**Who:** The builder. About 20 minutes.
**Controls:** RT-1, RT-5, EB-1, EB-2, AS-1, AS-3, AS-5, VO-4, PL-3

## Steps

1. **Pick the tier.** Use the table in [POL-01](../policies/POL-01-risk-tiers-and-roles.md). Write it down.
2. **Register the project.** Add a row to the project register: name, owner, tier, platform, what data it will touch.
3. **Find your reviewer** (Tier 2+). Get a name now, not the day before launch.
4. **Create the project with version history.**
   - On a code platform: create a Git repository (private) and make a first commit.
   - On an app-builder platform: turn on GitHub sync or version history.
5. **Protect secrets from day one.**
   - Create a `.gitignore` file containing at least `.env`, `.env.*`, and `*.key`.
   - Decide where secrets will live (platform secret manager or `.env`). Never in chat.
6. **Use test data only.** Make a development database or copy with fake data. Do not connect production.
7. **Set spending limits** on every paid service the project uses (AI, email, cloud).
8. **Write the project rules file.** For Claude Code, copy [`guardrails/claude-code/CLAUDE.md.template`](../guardrails/claude-code/CLAUDE.md.template) to `CLAUDE.md` in your project and fill in the blanks.
9. **Install the guardrails** (Claude Code users): copy the [guardrail settings and hook](../guardrails/) into the project's `.claude` folder.
10. **Write your "done means" list.** In plain words: what should the app do, and what must it never do? (See the [session guide](../guides/structuring-a-vibe-coding-session.md).)

Done? Tick off [Checklist A](../checklists/A-before-you-start.md).
