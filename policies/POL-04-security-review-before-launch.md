# POL-04 Security review before sharing or launch

**Purpose:** Stop apps from going live with doors left open.

**Plain-English background:**
- **Authentication** checks *who you are* (logging in).
- **Authorization** checks *what you're allowed to see* (your orders, not someone else's).
- **Row Level Security (RLS)** is a database setting that makes each row of data visible only to the right people. Without it, any logged-in (or even logged-out) user can read the whole table.
- **CSRF** (cross-site request forgery) is a trick where another website makes a logged-in user's browser do something without them knowing.

Missing login and access checks were the most common failure in the incident log, affecting thousands of apps. *(T3)*

## SR-1 No Tier 2+ app goes public without the security check

- Complete [PRO-02 Pre-launch security check](../procedures/PRO-02-pre-launch-security-check.md) and get sign-off from the technical reviewer before sharing a Tier 2 or 3 app outside your team. *(VC-03, VC-04, VC-16, VC-21, VC-23)*
- The `vibe-security-review` [skill](../skills/vibe-security-review/) can help the reviewer, but it does not replace the sign-off.

## SR-2 Every table has per-user access rules

- Every database table that stores user or business data has access rules (RLS or equivalent) switched on, and each rule is limited to the right user or role. *(VC-15, VC-18, VC-21)*
- "Allow all" or "public" rules require written justification from the reviewer.

## SR-3 Test as a stranger, not just as yourself

Testing only while logged in as yourself misses most access bugs. *(VC-16)* Before launch, test:

1. **Logged out:** can you see anything private?
2. **As a second user:** can user B see or change user A's data by changing a number in the web address?
3. **Wrong input:** what happens with a wrong password or code? Does the error reveal anything (such as the correct code)? *(VC-28)*

## SR-4 Login checks happen on the server

- Login and permission checks must happen on the server, not only in the browser. *(VC-22)*
- Use the platform's built-in authentication rather than custom code.
- Sign-up, password reset, and one-time-code endpoints must be rate limited and checked. *(VC-19)*
- Forms that change data have CSRF protection (most frameworks provide it; check it is turned on). *(VC-04)*

## SR-5 Payment and paywall checks happen on the server

- Whether a user has paid is decided by the server, never by something the browser can change. *(VC-20)*

## SR-6 Re-check old projects after platform fixes

- When a platform announces a security fix, check whether it applies to existing projects or only new ones, and re-run the security check on your older projects. *(VC-17)*
