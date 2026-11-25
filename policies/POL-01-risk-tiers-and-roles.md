# POL-01 Risk tiers and roles

**Purpose:** Let anyone in the organization build with AI, while matching the safety steps to how much damage a project could do.

**Applies to:** Everyone who uses an AI tool to create software, scripts, automations, spreadsheets with code, or apps. This includes people with no coding background.

## RT-1 Classify every project before you start

Pick the **highest** tier that fits. If you are unsure, pick the higher one.

| Tier | Plain description | Examples | What is required |
|---|---|---|---|
| **0 Sandbox** | Just for you, no real data, nothing shared. | Learning project, a game, a prototype with fake data. | Checklist A (before you start). |
| **1 Internal** | Used by you or your team, no personal or confidential data. | A script that tidies a shared spreadsheet of public info. | Checklists A–C. Tell your manager it exists. |
| **2 Sensitive** | Touches personal data, customer data, money, logins, or is shared outside your team. | A form that collects email addresses; a tool connected to your CRM. | Everything in Tier 1, **plus** the [pre-launch security check](../procedures/PRO-02-pre-launch-security-check.md) signed off by a named technical reviewer. |
| **3 Critical** | Production systems, customer-facing products, payments, or anything the business depends on. | A public app, a checkout flow, infrastructure changes. | Everything in Tier 2, **plus** an engineering owner who approves every release. Non-technical builders may prototype, but engineering ships. |

Record the tier in the project's `README` or in the [project register](#rt-5-keep-a-project-register).

## RT-2 Reviewers by tier

- **Tier 0–1:** self-review using the checklists.
- **Tier 2:** a named technical reviewer (someone who can read code) signs off before anyone outside the team uses it.
- **Tier 3:** an engineering owner approves each release. AI agents never get direct access to production. *(VC-12)*

## RT-3 Approved tools and modes

- Use only AI coding tools on the organization's approved list (see [POL-07](POL-07-platforms.md)).
- **Auto-approve modes are forbidden outside Tier 0.** These go by names like "Turbo", "YOLO", "auto-run", "bypass permissions", or "dangerously skip permissions". They let the AI run commands without asking you. *(VC-09, VC-10)*
- Organizations using Claude Code should deploy the [guardrail settings](../guardrails/) as managed settings, so this is enforced rather than just requested.

## RT-4 Training before use

Before building anything above Tier 0, a person must read:

1. [Best practices](../guides/best-practices.md)
2. [How to run a vibe coding session](../guides/structuring-a-vibe-coding-session.md)
3. The [checklists](../checklists/)

## RT-5 Keep a project register

Keep one shared list (a spreadsheet is fine) of every vibe-coded project above Tier 0, with: name, owner, tier, where it lives, what data it touches, reviewer, and the date it was last reviewed. A project that nobody remembers is a project nobody secures. *(VC-17, VC-26)*

## Roles

| Role | Responsibility |
|---|---|
| **Builder** | Follows the checklists, picks the tier honestly, asks for help early. |
| **Technical reviewer** | Runs or checks the pre-launch security check for Tier 2+. |
| **Engineering owner** | Owns Tier 3 releases, production access, and infrastructure. |
| **Tool admin** | Maintains the approved tools list and guardrail settings. |
| **Security contact** | Receives incident reports ([PRO-03](../procedures/PRO-03-ai-damage-incident-response.md), [PRO-04](../procedures/PRO-04-leaked-key-response.md)). |
