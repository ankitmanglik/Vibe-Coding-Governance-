# PRO-05 When the platform itself seems broken

**When:** Something stopped working and you didn't change anything: blank popups, "service error", "this app is blocked", or your project seems to have disappeared.
**Who:** The builder.
**Controls:** PL-3, PL-4, PL-5, PL-6

1. **Check whether it's just you.** Look at the platform's status page and recent posts in its community forum or issue tracker. *(VC-24, VC-27)*
2. **Wait and retry.** Many problems are temporary outages. Try again in an hour before changing code.
3. **Don't let the AI "fix" a platform outage.** Asking it to rewrite working code to dodge a temporary error creates new bugs.
4. **"App is blocked" or permission loops** (Google, Microsoft): this is usually an organization or platform policy. Contact your workspace admin with the error message and the script's name; don't try workarounds. *(VC-25)*
5. **Project seems missing:** check the project register for where it lives. For Google Apps Script, open [script.google.com](https://script.google.com) and look under "My projects". Scripts attached to a sheet and standalone scripts appear in different places. *(VC-26)*
6. **Frequent intermittent errors on long jobs:** ask your reviewer about adding retries with pauses, or splitting the job into smaller batches. *(VC-27)*
7. **Record it** in the project register's notes, so the next person knows.
