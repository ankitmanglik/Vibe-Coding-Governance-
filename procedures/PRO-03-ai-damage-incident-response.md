# PRO-03 When an AI tool damages something

**When:** An AI tool deleted, overwrote, sent, or changed something it shouldn't have, or won't stop.
**Who:** Whoever notices. Don't wait for permission to do step 1.
**Controls:** CL-4, EB-1, EB-3, VO-2

## 1. Stop it (first 2 minutes)

- Stop the AI: press its stop button, close the app, or shut the laptop lid if that's fastest. *(VC-10)*
- If it acts through a key or connection, **revoke or disable that key** in the service's settings. This stops it even if the app keeps running.
- If it is sending emails or messages, pause sending in the email provider. *(VC-28)*

## 2. Don't make it worse

- **Do not** ask the same AI session to "fix it" or "undo it" yet. It may not know what it did, and it may report things that are untrue. *(VC-01, VC-14)*
- Don't run cleanup or restore commands you don't understand.
- Take screenshots of what you see and save the chat or log.

## 3. Tell someone (within 15 minutes)

- Tier 2–3, or anything affecting other people: message your security contact and engineering owner.
- Say: what tool, what you asked it to do, what it did, what is affected, and what you have already done.

## 4. Recover

- **Files or code:** go back to your last Git save point (your reviewer can help). *(VC-02, VC-14)*
- **Database:** restore from backup or the platform's point-in-time recovery. Don't believe "rollback is impossible" until you've checked yourself. *(VC-01)*
- **Cloud provider:** contact their support quickly. Providers sometimes hold internal snapshots. *(VC-07)*

## 5. Learn (within a week)

Write a short note, with no blame:
1. What happened?
2. Which control in this toolkit would have prevented it, and why wasn't it in place?
3. What will change?

Share it, and consider adding it to [`incidents.csv`](../incidents/incidents.csv) through a contribution to this toolkit.
