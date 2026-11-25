# Traceability: incidents → controls

Every control in this toolkit exists because something went wrong for a real person or organization. This file shows the links in both directions.

- The full incident list (with summaries and sources) is in [`incidents.csv`](incidents.csv).
- Each control ID (for example `EB-2`) is defined in one of the [policies](../policies/).

## Themes

| Theme | What went wrong | Incidents |
|---|---|---|
| **T1** Destructive actions, no backup | The AI deleted or overwrote data, files, or whole systems, and there was no safe copy to go back to. | VC-01, 02, 07, 08, 09, 10, 13, 14 |
| **T2** Keys and permissions | Secret keys were exposed, or the AI was given far more access than the task needed. | VC-05, 08, 12, 13, 15, 20, 21, 22 |
| **T3** Login and data access | Apps let strangers sign in, see other people's data, or skip payment. | VC-03, 04, 15, 16, 17, 18, 19, 20, 21, 22, 23, 28 |
| **T4** Runaway loops and costs | Automations ran out of control, sending thousands of emails or running up huge bills. | VC-11, 28 |
| **T5** Unreviewed changes and AI over-confidence | Big changes went in unchecked, the AI claimed things that weren't true, or it "forgot" its safety rules. | VC-01, 05, 06, 10, 12, 28, 29, 30 |
| **T6** Platform dependence | The tool or platform itself broke, changed, or hid things. | VC-17, 19, 23, 24, 25, 26, 27 |

VC-31 is a reference entry (a forum directory), not an incident, so no control maps to it.

## Incident → controls

| ID | Incident | Controls that would have prevented or limited it |
|---|---|---|
| VC-01 | Replit agent deletes SaaStr production database during code freeze | EB-2, EB-4, EB-5, VO-2 |
| VC-02 | Solo builder's whole app deleted, no Git | EB-1, VO-1 |
| VC-03 | 5,000+ vibe-coded apps with no authentication | SR-1, PL-1, PL-2 |
| VC-04 | 15 AI-built apps, 69 flaws, zero CSRF protection | SR-1, SR-4 |
| VC-05 | Agent sessions leak secrets, run unreviewed changes, install fake packages | AS-1, VO-1, VO-6 |
| VC-06 | Replit project degrades as it grows; agent overwrites working code | VO-1, VO-5, PL-3 |
| VC-07 | `terraform destroy` wipes DataTalks.Club production | EB-2, EB-3, EB-4, EB-6 |
| VC-08 | PocketOS database and backups wiped in 9 seconds | AS-2, EB-2, EB-3, EB-4 |
| VC-09 | Antigravity "Turbo mode" wipes a whole drive | RT-3, EB-4 |
| VC-10 | Agent mass-deletes emails after forgetting its safety rules | RT-3, EB-4, CL-4, VO-4 |
| VC-11 | Multi-agent loop runs 11 days, costs $47,000 | AS-5, CL-1, CL-2 |
| VC-12 | Over-privileged agents cause outages and millions of lost orders | AS-2, RT-2, VO-1 |
| VC-13 | Over-scoped token in repo deletes production DB and backups | AS-2, AS-3, EB-3 |
| VC-14 | File move overwrites a whole project into one file | EB-1, EB-4 |
| VC-15 | Moltbook exposes 1.5M API tokens (browser-side key, no RLS) | AS-1, AS-3, AS-4, SR-2 |
| VC-16 | Lovable app with inverted login logic exposes 18,697 records | SR-1, SR-3 |
| VC-17 | Platform bug fixed only for new projects; old ones stay exposed | RT-5, SR-3, SR-6, PL-1 |
| VC-18 | CVE-2025-48757: missing RLS in ~170 apps | SR-2 |
| VC-19 | Base44 sign-up and one-time-password endpoints with no auth | SR-4, PL-1, PL-2 |
| VC-20 | EnrichLead: exposed keys and paywall bypass, shuts down | AS-1, AS-5, SR-5 |
| VC-21 | 5,600 apps scanned: 2,000+ flaws, 400+ exposed secrets | AS-1, AS-3, SR-1, SR-2 |
| VC-22 | 1 in 5 orgs have serious misconfigurations | AS-1, AS-4, SR-4 |
| VC-23 | Zero-click flaw in Orchids apps | SR-1, PL-1 |
| VC-24 | Blank Google permissions popup during an outage | PL-4 |
| VC-25 | "This app is blocked" authorization loop | PL-4, PL-6 |
| VC-26 | Apps Script project "disappears" | RT-5, PL-3, PL-5 |
| VC-27 | Intermittent Drive service errors | PL-4 |
| VC-28 | Email storms (1,832 and ~100,000 emails), login leaking its own code | CL-2, CL-3, SR-3, VO-2 |
| VC-29 | Vibe coders can't diagnose real bugs | VO-3, VO-5 |
| VC-30 | "State drift" on large AI edits | VO-1 |

## Control → incidents

| Control | Short name | Incidents |
|---|---|---|
| RT-2 | Reviewer required by risk tier | VC-12 |
| RT-3 | No auto-approve modes outside sandbox | VC-09, 10 |
| RT-5 | Keep a register of every project | VC-17, 26 |
| AS-1 | Never paste secrets into chat or code | VC-05, 15, 20, 21, 22 |
| AS-2 | Least-privilege, no production tokens for AI | VC-08, 12, 13 |
| AS-3 | No secrets in the repository, scan before push | VC-13, 15, 21 |
| AS-4 | Browser keys are public | VC-15, 22 |
| AS-5 | Spending limits on every key | VC-11, 20 |
| EB-1 | Git from minute one, checkpoint before changes | VC-02, 14 |
| EB-2 | AI works only in a development copy | VC-01, 07, 08 |
| EB-3 | Backups stored separately and tested | VC-07, 08, 13 |
| EB-4 | A human confirms destructive commands | VC-01, 07, 08, 09, 10, 14 |
| EB-5 | Code freeze means no AI write access | VC-01 |
| EB-6 | Infrastructure changes only by a technical owner | VC-07 |
| SR-1 | Security check before sharing or launch | VC-03, 04, 16, 21, 23 |
| SR-2 | Every table has per-user access rules | VC-15, 18, 21 |
| SR-3 | Test as a stranger and as another user | VC-16, 17, 28 |
| SR-4 | Server-side login checks and CSRF protection | VC-04, 19, 22 |
| SR-5 | Payment checks enforced on the server | VC-20 |
| SR-6 | Re-check old projects after platform fixes | VC-17 |
| CL-1 | Hard budget caps and alerts | VC-11 |
| CL-2 | Limits and kill switch on automations | VC-11, 28 |
| CL-3 | Sending caps and test mode for email | VC-28 |
| CL-4 | A stop button that really works | VC-10 |
| VO-1 | Small changes, one at a time | VC-02, 05, 06, 12, 30 |
| VO-2 | Verify the AI's claims yourself | VC-01, 28 |
| VO-3 | Describe and test the expected behaviour | VC-29 |
| VO-4 | Keep rules in a project file, restart long sessions | VC-10 |
| VO-5 | Know when to bring in an engineer | VC-06, 29 |
| VO-6 | Check packages before installing | VC-05 |
| PL-1 | Approved platforms list | VC-03, 17, 19, 23 |
| PL-2 | Don't assume platform defaults are secure | VC-03, 19 |
| PL-3 | Keep an exit route (code in Git) | VC-06, 26 |
| PL-4 | Check platform status before debugging | VC-24, 25, 27 |
| PL-5 | Record where things live and who owns them | VC-26 |
| PL-6 | Admin allowlist for third-party app permissions | VC-25 |

RT-1 (classify every project) and RT-4 (training before use) apply to all incidents: they are what makes the other controls happen.
