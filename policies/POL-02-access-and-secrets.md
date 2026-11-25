# POL-02 Access and secrets

**Purpose:** Stop secret keys from leaking, and stop AI tools from having more power than the task needs.

**Plain-English background:** A *secret* (also called an API key, token, or password) is like a house key for a service. Anyone who has it can act as you, spend your money, or read your data. AI agents will use any key they can find, including a key that can delete everything. *(VC-08, VC-13)*

## AS-1 Never paste secrets into chat or code

- Do not paste keys, passwords, or tokens into an AI chat, prompt, or source file. *(VC-05, VC-15, VC-20, VC-21, VC-22)*
- Store secrets in the platform's secret manager or in environment variables (a `.env` file that is never shared or committed).
- If you are unsure whether something is a secret, treat it as one.

## AS-2 Least privilege: the smallest key that does the job

- Give AI tools only keys scoped to **one project, one environment, and the minimum actions** (for example, read-only).
- **AI tools never receive production, admin, owner, or billing keys.** *(VC-08, VC-12, VC-13)*
- Prefer keys that expire (hours or days, not forever).
- Delete keys you no longer use.

## AS-3 No secrets in the repository

- Add `.env` and similar files to `.gitignore` before the first commit.
- Turn on secret scanning in your code host (for example, GitHub secret scanning and push protection).
- The [guardrail hook](../guardrails/) warns when the AI tries to write something that looks like a key into a file. *(VC-13, VC-15, VC-21)*

## AS-4 Anything in the browser is public

- Code that runs in the user's browser (the "front end" or "client") can be read by anyone. A key placed there is published to the world. *(VC-15, VC-22)*
- Only keys designed to be public (often called "publishable" or "anon" keys) may appear in the browser, and only when the database's access rules ([SR-2](POL-04-security-review-before-launch.md)) are switched on.

## AS-5 Spending limits on every key

- Every paid API key (AI models, email, SMS, cloud) must have a hard monthly spending cap and an alert at 50% and 80%. *(VC-11, VC-20)*

## What to do if a secret leaks

Follow [PRO-04 Leaked key response](../procedures/PRO-04-leaked-key-response.md) immediately. Deleting the message or file is **not** enough: the key must be replaced.
