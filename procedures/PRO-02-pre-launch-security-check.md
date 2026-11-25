# PRO-02 Pre-launch security check

**When:** Before a Tier 2 or 3 app is used by anyone outside the builder's team, and again after any major change.
**Who:** The builder prepares; the technical reviewer verifies and signs off.
**Controls:** SR-1 to SR-6, AS-1, AS-3, AS-4, AS-5, CL-1 to CL-3, EB-3

Record the result of each check as **Pass**, **Fail**, or **N/A** (with a reason). Any **Fail** blocks launch.

## 1. Secrets *(VC-05, 13, 15, 20, 21, 22)*

- [ ] Run a secret scanner over the whole repository and its history (for example GitHub secret scanning, `gitleaks`, or `trufflehog`). No live secrets found.
- [ ] Open the live app in a browser, open the developer tools (F12), and search the page source and network requests for `key`, `secret`, `token`, `sk_`, `password`. Only publishable keys appear.
- [ ] Every key used has the minimum permissions and a spending cap.

## 2. Login *(VC-03, 04, 16, 19, 22, 28)*

- [ ] Uses the platform's built-in authentication, not custom login code.
- [ ] Every private page and every data request checks login **on the server**.
- [ ] Sign-up, login, password reset, and one-time-code endpoints are rate limited.
- [ ] A wrong password or code shows a generic error and reveals nothing else (check the network response, not just the screen).
- [ ] Forms that change data have CSRF protection, or the framework's protection is confirmed on.

## 3. Data access *(VC-15, 16, 17, 18, 21)*

- [ ] Row Level Security (or equivalent) is ON for every table.
- [ ] Every access rule is limited to the owning user or a role; none are "allow all" without written justification.
- [ ] **Stranger test:** logged out, try every page and data address. Nothing private is visible.
- [ ] **Neighbour test:** with two test accounts, user B cannot read or change user A's data, including by changing IDs in the web address or request.

## 4. Money *(VC-20)*

- [ ] Paid features are checked on the server. Changing something in the browser does not unlock them.

## 5. Runaway protection *(VC-11, 28)*

- [ ] Every scheduled job, loop, or agent has a maximum run count or time and an off switch.
- [ ] Email/SMS sending has caps and was tested in sandbox mode.
- [ ] Budget caps and alerts are set on all paid services.

## 6. Recovery *(VC-07, 08, 13)*

- [ ] Backups exist, are stored outside the production account's reach, and one restore has been tested.
- [ ] The app's code is in Git and the latest version is pushed.

## 7. Platform *(VC-17, 23)*

- [ ] The platform is on the approved list for this tier.
- [ ] Any recent platform security notices have been checked for whether they affect this project.

## Sign-off

| Item | Value |
|---|---|
| Project | |
| Tier | |
| Builder | |
| Reviewer | |
| Date | |
| Result | Pass / Fail |
| Notes | |

Tip: the reviewer can ask Claude to run the `vibe-security-review` [skill](../skills/vibe-security-review/) to prepare findings. A person still checks and signs.
