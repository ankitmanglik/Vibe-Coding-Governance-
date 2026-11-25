# POL-07 Choosing and relying on vibe coding platforms

**Purpose:** Choose platforms that are safe enough, don't assume their defaults protect you, and keep a way out.

## PL-1 Approved platforms list

- The tool admin keeps a list of approved AI coding tools and app-building platforms, with the highest tier each may be used for. *(VC-03, VC-17, VC-19, VC-23)*
- Before approving a platform, check: does it separate dev and prod, offer backups, support secret storage, switch on access rules by default, and publish security fixes?

## PL-2 Platform defaults are not security

- "The platform handles security" is not true by default. Apps on several platforms were public with no login because nobody switched it on. *(VC-03, VC-19)*
- Run the [pre-launch security check](../procedures/PRO-02-pre-launch-security-check.md) regardless of platform.

## PL-3 Keep an exit route

- Make sure your code can be exported, ideally synced to a Git repository you control. Projects outgrow platforms. *(VC-06, VC-26)*

## PL-4 Check the platform before debugging your own work

- When something suddenly stops working with no change on your side (blank popups, "service error", authorization loops), check the platform's status page and community forums first, then retry later. *(VC-24, VC-25, VC-27)*
- See [PRO-05 Platform problems](../procedures/PRO-05-platform-problems.md).

## PL-5 Record where things live and who owns them

- Note where each script or app lives (for example, a Google Apps Script attached to a specific sheet versus a standalone project) and which account owns it. *(VC-26)*
- Add it to the project register ([RT-5](POL-01-risk-tiers-and-roles.md)).

## PL-6 Admins control third-party app permissions

- Workspace admins (Google Workspace, Microsoft 365) keep an allowlist of scripts and apps allowed to access organization data, and a documented way to request access. *(VC-25)*
