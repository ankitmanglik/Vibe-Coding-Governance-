# POL-03 Environments, backups, and destructive actions

**Purpose:** Make sure an AI mistake can always be undone.

**Plain-English background:**
- **Git** is an "undo history" for your whole project. Each save point is called a *commit*.
- **Development (dev)** is a practice copy where mistakes are fine. **Production (prod)** is the real thing that real people use.
- A **destructive action** is anything that deletes, overwrites, or resets data or files.

In the incident log, eight separate failures were the AI deleting something with no way back. *(T1)*

## EB-1 Git from minute one

- Every project above Tier 0 uses Git (or the platform's equivalent version history) from the first session. *(VC-02, VC-14)*
- Make a save point (commit) **before** asking the AI for any change, and after each change that works.
- Push to a remote copy (for example, a private GitHub repo) at least daily, so a wiped laptop is not a lost project.

## EB-2 AI works only in a development copy

- AI tools work on a development copy with test data, never directly on production. *(VC-01, VC-07, VC-08)*
- Production data must not be reachable from the AI's environment: no production connection strings, no production keys ([AS-2](POL-02-access-and-secrets.md)).
- Changes reach production only through a reviewed release ([RT-2](POL-01-risk-tiers-and-roles.md)).

## EB-3 Backups stored separately, and tested

- Backups must live **somewhere the production key cannot delete**: a different account, project, or storage location. *(VC-08, VC-13)*
- Test a restore at least once per quarter for Tier 2 and 3. A backup you have never restored is a hope, not a backup.
- Turn on the platform's point-in-time recovery or deletion protection where offered. *(VC-07)*

## EB-4 A human confirms every destructive action

- The AI must ask, and a person must say yes, before: deleting or moving files in bulk, deleting databases or tables, resetting Git history, force-pushing, running infrastructure teardown commands, or sending messages in bulk. *(VC-01, VC-07, VC-08, VC-09, VC-10, VC-14)*
- Confirmations must show **exactly what will be affected**, not just "OK to proceed?".
- In Claude Code, this is enforced by the [guardrail settings and hook](../guardrails/).

## EB-5 A code freeze means the AI has no write access

- Saying "don't change anything" in a chat is not a freeze. During a freeze, remove the AI's ability to write (read-only keys, or stop the agent). *(VC-01)*

## EB-6 Infrastructure is for technical owners

- Commands that create or destroy cloud infrastructure (for example `terraform apply/destroy`, `kubectl delete`, cloud CLI delete commands) are run only by the engineering owner, after reading the plan of what will change. *(VC-07)*
