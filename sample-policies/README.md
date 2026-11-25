# Sample policies: ready to adopt

This folder contains a formal policy and forms that a company can copy, customize, and approve. They are a starting point, not legal advice: have your security, legal, and HR teams review them before adoption.

| File | What it is |
|---|---|
| [AI-Assisted-Development-Policy.md](AI-Assisted-Development-Policy.md) | The master policy. One document covering tiers, tools, secrets, environments, review, release, incidents, training, and exceptions. |
| [forms/Employee-Acknowledgement-Form.md](forms/Employee-Acknowledgement-Form.md) | Staff sign it to confirm they have read the policy and will follow it. |
| [forms/Exception-Request-Form.md](forms/Exception-Request-Form.md) | Request and approve a time-limited exception to the policy. |
| [forms/Project-Register-Template.csv](forms/Project-Register-Template.csv) | Opens in Excel or Google Sheets. One row per AI-assisted project. |

The explanatory policies in [`../policies/`](../policies/) give the reasoning and incident links behind each rule. This folder is the "signed" version.

## How to adopt (8 steps)

1. **Copy** this folder into your policy library. Convert to Word or your policy tool if needed.
2. **Fill the blanks.** Search for `[` and replace every bracketed item: company name, roles, timeframes, links.
3. **Choose your tool list.** Decide which AI tools are approved, and for which tiers (policy section 6).
4. **Name the people.** Who is the policy owner, the security contact, and the pool of technical reviewers?
5. **Set up the register.** Import the project register template into a shared spreadsheet.
6. **Turn on the guardrails.** Ask IT to deploy the [Claude Code managed settings](../guardrails/) and the [Claude skills](../skills/).
7. **Approve and publish.** Get sign-off through your normal policy approval route, then publish it with the [checklists](../checklists/) and [guides](../guides/).
8. **Train and acknowledge.** Run a short session using the guides, and collect signed acknowledgement forms.

**Tip for small companies:** you can start with sections 5–10 and 12 only, and add the rest as you grow.

## Mapping to common standards

Auditors often ask how a policy relates to frameworks you already follow. This table is a guide only; confirm it with your auditor.

| Policy section | ISO/IEC 27001:2022 Annex A | SOC 2 (Trust Services Criteria) |
|---|---|---|
| 4 Roles | 5.2 Information security roles and responsibilities | CC1.3 |
| 5 Risk tiers and register | 5.9 Inventory of information and other associated assets; 5.12 Classification of information | CC3.2 |
| 6 Approved tools | 5.19 Information security in supplier relationships; 5.23 Information security for use of cloud services | CC9.2 |
| 7 Secrets and access | 5.17 Authentication information; 8.2 Privileged access rights; 8.3 Information access restriction | CC6.1, CC6.3 |
| 8 Environments and backups | 8.13 Information backup; 8.31 Separation of development, test and production environments | CC6.1, A1.2 |
| 9 Working with AI output | 8.25 Secure development life cycle; 8.28 Secure coding | CC8.1 |
| 10 Security review | 8.5 Secure authentication; 8.29 Security testing in development and acceptance | CC7.1, CC8.1 |
| 11 Release to production | 8.32 Change management | CC8.1 |
| 12 Incidents | 5.24 – 5.26 Information security incident management | CC7.3 – CC7.5 |
| 13 Training | 6.3 Information security awareness, education and training | CC1.4, CC2.2 |
| 14 Exceptions | 5.1 Policies for information security | CC5.3 |
