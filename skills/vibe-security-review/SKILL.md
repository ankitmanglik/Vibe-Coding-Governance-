---
name: vibe-security-review
description: Review a vibe-coded or AI-generated app for the security failures seen most often in real incidents (exposed secrets, missing login checks, missing Row Level Security, CSRF, paywall bypass, runaway loops). Use before an app is shared or launched, or when asked whether an app is secure.
---

# Vibe security review

Produce findings that a technical reviewer can verify and a non-technical builder can understand. This review **supports** the toolkit's pre-launch security check (`procedures/PRO-02`); it does not replace a human sign-off.

## Rules

- **Read-only.** Do not change code, data, settings, or keys during the review. Suggest fixes; don't apply them unless asked afterwards.
- **Never print a full secret.** Show the file, line, and the first four characters only.
- Say exactly what you checked and how. If you could not check something (for example, live database rules you can't see), mark it **Not verified**, never Pass.
- Don't run the app, tests, or scanners without the user's explicit OK.

## What to check

Work through each area. For each item record **Pass / Fail / Not verified / N/A**, with evidence (file and line, or the reason).

### 1. Secrets *(VC-05, 13, 15, 20, 21, 22)*
- Search the code and config for likely secrets: `sk_`, `sk-`, `AKIA`, `ghp_`, `xox`, `-----BEGIN`, `password=`, `secret`, `token`, `api_key`, long random strings.
- Is `.env` (and similar) in `.gitignore`? Has a secret file ever been committed? (`git log --all -- .env`, if Git is available.)
- Does any secret appear in front-end/browser code? Only publishable or anon keys are acceptable there.

### 2. Authentication *(VC-03, 19, 22, 28)*
- Is a standard auth provider used, or custom login code?
- Is every private route or API endpoint protected **on the server**? List any that aren't.
- Are sign-up, login, reset, and one-time-code endpoints rate limited?
- Do error responses for wrong passwords or codes leak information (for example, returning the correct code)?
- Is there logic that could be inverted (for example, `if (!user)` granting access)? *(VC-16)*

### 3. Authorization and data access *(VC-15, 16, 17, 18, 21)*
- For Supabase/Postgres: is RLS enabled on every table? Are policies scoped with `auth.uid()` or roles, or are any `true` / public?
- For other backends: does every query filter by the current user or check ownership?
- Can an ID in a URL or request be changed to reach another user's record (BOLA)?

### 4. CSRF and request safety *(VC-04)*
- Do state-changing requests have CSRF protection, or use an auth scheme that isn't vulnerable (for example, bearer tokens not sent automatically by the browser)?

### 5. Payments and paywalls *(VC-20)*
- Is paid access checked on the server, from the payment provider's records?

### 6. Runaway protection *(VC-11, 28)*
- Loops, retries, schedulers, webhooks, agents: is there a maximum count, time limit, or kill switch?
- Email/SMS: are there caps and a test mode? Could one event trigger repeated sends?

### 7. Dependencies *(VC-05)*
- Do all packages exist, appear widely used, and look correctly spelled (no look-alikes)?

### 8. Recovery *(VC-07, 08, 13)*
- Is there evidence of backups stored separately from production? (Usually **Not verified** from code alone: ask.)

## Output format

Start with a plain-language summary of three to five lines for the builder: is it safe to share, and what are the most important fixes?

Then a table:

| # | Area | Check | Result | Evidence | Plain-words risk | Suggested fix |
|---|---|---|---|---|---|---|

Order the findings: **Fail** first (most severe on top), then **Not verified**, then Pass.

End with: "A technical reviewer must confirm these findings and complete the sign-off in PRO-02 before launch."
