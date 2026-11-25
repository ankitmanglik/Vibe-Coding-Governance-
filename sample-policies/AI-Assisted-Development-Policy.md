# [COMPANY NAME] AI-Assisted Development ("Vibe Coding") Policy

| | |
|---|---|
| **Policy ID** | [e.g. IS-POL-0XX] |
| **Version** | 1.0 |
| **Owner** | [Role, e.g. Chief Information Security Officer] |
| **Approved by** | [Name, role] |
| **Effective date** | [DD Month YYYY] |
| **Next review** | [12 months after effective date] |
| **Classification** | Internal |

> **How to use this template:** Replace every `[BRACKETED]` item. Delete these grey notes. Sections marked *(optional)* can be removed. Control IDs in brackets (for example `[EB-2]`) link each rule to the Vibe Coding Governance Toolkit and the real incidents behind it; you may keep or delete them.

---

## 1. Purpose

[COMPANY NAME] encourages employees to use AI tools to build software, automations, and apps. This policy makes sure that work does not put our data, customers, money, or systems at risk. It sets the minimum rules everyone must follow, scaled to how much harm a project could cause.

## 2. Scope

This policy applies to:

- all employees, contractors, and temporary staff ("**Users**");
- any software, script, automation, spreadsheet code, workflow, or app that is created or changed with the help of an AI tool ("**AI-Assisted Project**"), whether or not the User can read code;
- all AI coding assistants, AI agents, and AI app-building platforms ("**AI Tools**"), whether provided by [COMPANY NAME] or not, when used for [COMPANY NAME] work or with [COMPANY NAME] data.

It does not replace the [Information Security Policy], [Acceptable Use Policy], [Data Protection Policy], or [Change Management Policy]. Where they conflict, the stricter rule applies.

## 3. Definitions

| Term | Meaning |
|---|---|
| **AI Agent** | An AI Tool that can take actions itself, such as running commands, editing files, or calling services. |
| **Secret** | Any password, API key, access token, private key, or connection string. |
| **Production** | Any system, data, or environment used by real customers, employees, or business processes. |
| **Development Environment** | A separate copy for building and testing, containing only test or anonymised data. |
| **Destructive Action** | Any action that deletes, overwrites, moves in bulk, resets, or sends in bulk (files, data, infrastructure, messages). |
| **Technical Reviewer** | A person named by [Engineering / IT] who can assess code and security. |
| **Engineering Owner** | The engineering team or person accountable for a Production system. |
| **Approved Tools List** | The list of AI Tools approved under section 6, maintained by [IT / Security]. |
| **Project Register** | The central record of AI-Assisted Projects described in section 5.3. |

## 4. Roles and responsibilities

| Role | Responsibilities |
|---|---|
| **Users** | Follow this policy and the published checklists; classify projects honestly; report incidents immediately. |
| **Managers** | Make sure their team members complete training; are told about all Tier 1+ projects in their team. |
| **Technical Reviewers** | Complete the pre-launch security check for Tier 2+ projects before release. |
| **Engineering Owners** | Approve every Tier 3 release; own Production access, infrastructure, and backups. |
| **[IT / Security]** | Maintain the Approved Tools List, guardrail configuration, and Project Register; receive incident reports; approve exceptions. |
| **Policy Owner** | Keep this policy current and review it at least annually. |

## 5. Risk tiers and project governance

### 5.1 Classification [RT-1]

Before starting, Users **must** classify every AI-Assisted Project into the highest applicable tier:

| Tier | Description | Minimum requirements |
|---|---|---|
| **0 Sandbox** | Personal or learning use; test data only; not shared. | Sections 7 and 8 apply. |
| **1 Internal** | Used within one team; no personal, confidential, or financial data. | Tier 0 + register the project + inform manager. |
| **2 Sensitive** | Handles personal, confidential, customer, or financial data; uses logins; or is used outside the team. | Tier 1 + named Technical Reviewer + pre-launch security check (section 10). |
| **3 Critical** | Production, customer-facing, payment, or business-critical systems; infrastructure. | Tier 2 + Engineering Owner approval of every release (section 11). |

If unsure, Users **must** choose the higher tier. Users **must** re-classify a project when its use or data changes.

### 5.2 Reviewers [RT-2]

Tier 2 projects **must** have a named Technical Reviewer before development begins. Tier 3 projects **must** have an Engineering Owner.

### 5.3 Project Register [RT-5]

Every Tier 1+ project **must** be recorded in the Project Register with: name, owner, tier, platform and location, data used, reviewer, and last review date. Projects **must** be reviewed [at least annually] and retired projects removed or archived.

## 6. Approved AI Tools and platforms [RT-3, PL-1, PL-2, PL-6]

6.1 Users **must** use only AI Tools on the Approved Tools List for [COMPANY NAME] work, within the maximum tier listed for each tool.

6.2 [IT / Security] **must** assess each tool before approval, including: separation of development and Production, backup and recovery, secret storage, access-control defaults, audit logging, data retention and training use, and the vendor's security-fix process.

6.3 Users **must not** assume a platform's default settings are secure.

6.4 Modes that let an AI Tool act without per-action human approval (for example "auto-run", "turbo", "YOLO", "bypass permissions") **must not** be used outside Tier 0. Where possible, [IT / Security] **will** enforce this through managed configuration.

6.5 Third-party apps and scripts that access [Google Workspace / Microsoft 365] data **must** be on the admin allowlist.

## 7. Secrets and access [AS-1 – AS-5]

7.1 Users **must not** paste Secrets into an AI Tool's chat or prompt, or write them into source code.

7.2 Secrets **must** be stored in an approved secret manager or environment-variable file that is excluded from version control.

7.3 AI Tools and AI Agents **must** be given only the minimum access needed: scoped to one project and one environment, read-only where possible, and time-limited where supported.

7.4 AI Tools and AI Agents **must not** be given Production, administrator, owner, or billing credentials.

7.5 Secrets **must not** appear in code that runs in a user's browser or device, except keys designed to be public, and then only with access controls enabled (section 10.2).

7.6 Every paid service used by an AI-Assisted Project **must** have a hard spending limit and alerts.

7.7 Repositories **must** have secret scanning enabled where the platform supports it.

## 8. Environments, backups, and destructive actions [EB-1 – EB-6]

8.1 Every Tier 1+ project **must** use version control (Git or the platform's version history) from the start, with a copy stored outside the User's device.

8.2 AI Tools **must** work only in a Development Environment. Production data and credentials **must not** be reachable from it.

8.3 Backups of Tier 2+ data **must** be stored where Production credentials cannot delete them, and a restore **must** be tested at least [quarterly].

8.4 A person **must** explicitly approve every Destructive Action proposed by an AI Tool, after seeing exactly what will be affected.

8.5 During a declared change freeze, AI Tools **must** have no write access to the affected systems. An instruction in a chat is not sufficient.

8.6 Infrastructure creation or teardown (for example `terraform apply/destroy`) **must** be performed only by the Engineering Owner after reviewing the planned changes.

## 9. Working with AI output [VO-1 – VO-6, CL-1 – CL-4]

9.1 Users **must** make changes in small steps, check each step works, and save a version before the next.

9.2 Users **must not** rely on an AI Tool's claims that work is complete, tested, secure, or irreversible without independent verification.

9.3 Users **must** write down, before building, what the project must and must not do, and check it after changes.

9.4 Project rules **must** be kept in a file the AI Tool reads each session (for example `CLAUDE.md`), not only in chat.

9.5 Users **must** check that any software package an AI Tool proposes is genuine and maintained before installing it.

9.6 Every loop, schedule, automation, or AI Agent **must** have a maximum run count or duration and a tested way to stop it.

9.7 Features that send email, SMS, or other messages **must** use test mode until reviewed and **must** have sending limits.

9.8 Users **must** seek technical help when a problem recurs after three attempts, when the project's tier increases, or when they do not understand a proposed change.

## 10. Security review before release [SR-1 – SR-6]

10.1 A Tier 2+ project **must not** be made available outside the building team until a Technical Reviewer has completed and signed the pre-launch security check ([link to PRO-02]).

10.2 The check **must** confirm at least that:
- no Secrets are exposed in code, history, or the browser;
- authentication uses an approved provider and is enforced on the server;
- every data store has access rules (for example Row Level Security) limited to the right user or role;
- the app has been tested logged out, as a second user, and with invalid inputs;
- state-changing requests are protected against CSRF;
- payment and entitlement checks are enforced on the server;
- loops and messaging have limits; and
- backups and version history exist.

10.3 The security check **must** be repeated after any major change, and when a platform announces a security fix that may affect existing projects.

## 11. Release to Production (Tier 3)

11.1 Tier 3 changes **must** be approved by the Engineering Owner and released through [COMPANY NAME]'s standard [change management process].

11.2 AI Tools **must not** deploy directly to Production.

## 12. Incidents

12.1 Users **must** immediately stop an AI Tool that has taken, or is taking, an unexpected or harmful action, and revoke its access if needed.

12.2 Users **must** report the incident to [security contact / channel] within [15 minutes / 1 hour], following [link to PRO-03].

12.3 Any Secret that may have been exposed **must** be replaced (rotated) immediately, following [link to PRO-04]. Deleting it from a file or message is not sufficient.

12.4 Incident reviews **will** be blame-free and focus on improving controls.

## 13. Training

13.1 Before working on any Tier 1+ project, Users **must** complete [training name], covering the toolkit's best practices, session guide, and checklists, and sign the acknowledgement form.

13.2 Refresher training **must** be completed [annually].

## 14. Exceptions

14.1 Exceptions **must** be requested using the Exception Request Form and approved by [IT / Security] (and the Engineering Owner for Tier 3) **before** the exception takes effect.

14.2 Exceptions **must** have an expiry date of no more than [6 months] and compensating controls.

## 15. Compliance and enforcement

15.1 [IT / Security] may audit AI-Assisted Projects and AI Tool configuration for compliance.

15.2 Non-compliance may result in removal of AI Tool access, removal of the project from use, and action under [COMPANY NAME]'s [disciplinary policy]. Good-faith reporting of mistakes and incidents will not be penalised.

## 16. Related documents

- Vibe Coding Governance Toolkit: checklists A–D, procedures PRO-01 to PRO-05, best practices, session guide
- [Information Security Policy]
- [Acceptable Use Policy]
- [Data Protection / Privacy Policy]
- [Change Management Policy]
- [Incident Response Plan]

## 17. Revision history

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | [date] | [name] | Initial adoption, based on the Vibe Coding Governance Toolkit v0.1 |
