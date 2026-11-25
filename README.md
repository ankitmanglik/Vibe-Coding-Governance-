# Vibe Coding Governance Toolkit

Open source **policies, procedures, checklists, guides, Claude skills, and guardrails** that let anyone in an organization build software with AI ("vibe coding") without deleting production, leaking keys, or shipping apps that let strangers in.

Every rule here traces back to a real, public incident from 2025–2026. See the [incident log](incidents/incidents.csv) and the [traceability table](incidents/TRACEABILITY.md).

## Why this exists

Thirty public incidents show the same six failures repeating:

| | Failure | Example |
|---|---|---|
| T1 | AI deletes things and there's no backup | An agent wiped a production database during a code freeze, then said rollback was impossible. |
| T2 | Keys and permissions too broad or exposed | An over-scoped token let an agent delete a database **and** its backups in one call. |
| T3 | Missing login and data-access checks | Thousands of AI-built apps exposed user data because access rules were never switched on. |
| T4 | Runaway loops and costs | A multi-agent loop ran for 11 days and cost $47,000. |
| T5 | Unreviewed changes, over-confident AI | Agents rewrote working code, and one claimed "no issues" in code sending thousands of emails. |
| T6 | Platform dependence | Outages, policy blocks, and fixes applied only to new projects. |

## Start here

**I'm a builder with no coding background**
1. Read [Best practices](guides/best-practices.md) (10 minutes).
2. Read [How to run a vibe coding session](guides/structuring-a-vibe-coding-session.md).
3. Use the [checklists](checklists/): A before you start, B every session, C before you share, D if something goes wrong.
4. Unfamiliar word? See the [glossary](guides/glossary.md).

**I'm adopting this for my organization**
1. Adopt the [sample policy](sample-policies/) (fill in the blanks); the [policies](policies/) folder explains the reasoning behind each rule.
2. Publish the [procedures](procedures/) where people will find them.
3. Deploy the [Claude skills](skills/) and the [guardrails](guardrails/).
4. Start a project register (POL-01, RT-5).

## What's inside

```
sample-policies/ Ready-to-adopt master policy, forms, adoption guide, ISO 27001 / SOC 2 mapping
policies/       Org rules, each control with an ID (e.g. EB-2) and the incidents behind it
  POL-01 Risk tiers and roles          POL-05 Cost and automation limits
  POL-02 Access and secrets            POL-06 Verifying AI output
  POL-03 Environments and backups      POL-07 Platforms
  POL-04 Security review before launch
procedures/     Step-by-step
  PRO-01 New project setup             PRO-04 Leaked key response
  PRO-02 Pre-launch security check     PRO-05 Platform problems
  PRO-03 When an AI damages something
checklists/     Plain-language checklists for non-technical builders (A-D)
guides/         Best practices, session structure, glossary
skills/         Claude skills
  safe-vibe-coding      Always-on guardrails while building
  vibe-session-coach    Walks a non-technical user through a structured session
  vibe-security-review  Read-only security review before launch
  launch-readiness      "Is this ready to share?" by risk tier
guardrails/     Claude Code settings + a Python 3.14 safety hook
incidents/      The incident log and traceability table
```

## Using the Claude skills

- **Claude Code:** copy a skill folder (for example `skills/safe-vibe-coding/`) into your project's `.claude/skills/` folder, or into `~/.claude/skills/` to use it everywhere.
- **Claude apps:** upload the skill folder as a zip in Settings → Capabilities → Skills.
- **Organizations:** admins can make the skills available to everyone.

## Status

Version 0.1, a first draft for review. The guardrail hook hasn't been tested yet; try it in a sandbox project first.

## Contributing

New incidents, fixes, and guardrails for other tools are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).

## Disclaimer

This toolkit reduces risk; it doesn't eliminate it. It is not legal or compliance advice. Incident summaries are based on public reports linked in the log and may contain inaccuracies.
