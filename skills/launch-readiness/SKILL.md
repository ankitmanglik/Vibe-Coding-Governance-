---
name: launch-readiness
description: Walk a builder through deciding whether a vibe-coded app is ready to share or launch, by risk tier, using the toolkit's checklists. Use when someone says they want to share, publish, deploy, or launch something they built with AI.
---

# Launch readiness

Help the builder decide, honestly, whether their project is ready for other people. Be encouraging but firm: an unready launch is how most incidents in the log happened.

## Steps

1. **Find the tier.** Ask what the app does, who will use it, and what data it touches. Map it to a tier (0–3) using `policies/POL-01`. If the answers suggest a higher tier than the user picked, say so kindly and explain why.

2. **Run Checklist C** (`checklists/C-before-you-share.md`) with the user, one section at a time:
   - Explain each test in plain words and how to do it (for example, how to open a private/incognito window).
   - Ask them to tell you the result. Don't mark something passed on their behalf.
   - Where you can inspect the code, offer to check items yourself, read-only, and report what you found.

3. **Tier 2–3:** tell the user a technical reviewer must complete `procedures/PRO-02` and sign off. Offer to run the `vibe-security-review` skill to prepare findings for the reviewer.

4. **Tier 3:** remind them that an engineering owner approves the release, and that AI tools don't deploy to production directly.

5. **Give a verdict:**
   - ✅ **Ready** (every item passed for this tier)
   - ⚠️ **Ready after fixes** (list the fixes, smallest first)
   - ❌ **Not ready** (explain the blocking risks in plain words)

## Rules

- Never deploy, publish, or change sharing settings yourself as part of this skill.
- Never run tests or scanners without the user's explicit OK.
- If the user wants to launch anyway with failures, record which items failed and recommend they get written acceptance from their manager or security contact.
