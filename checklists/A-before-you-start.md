# Checklist A: Before you start a new project

Answer each question. Tick it only if the answer is **yes**.

## What am I building?

- [ ] **I can describe what I'm building in two sentences.**
  *Why: if you can't explain it, the AI can't build it properly.*
- [ ] **I know who will use it**: just me / my team / people outside my team / customers.
- [ ] **I know whether it will touch anything private**: names, emails, phone numbers, money, passwords, health or customer data.
- [ ] **I've picked my risk level** using this simple test:

  | If it's... | Your level |
  |---|---|
  | Just for me, with made-up data | 🟢 Level 0: go ahead |
  | For my team, nothing private | 🟡 Level 1: tell your manager |
  | Touches private data, money, or people outside the team | 🟠 Level 2: you need a technical reviewer |
  | Customers or the business depend on it | 🔴 Level 3: engineering must own the launch |

- [ ] **For Level 2 or 3: I know who my technical reviewer is**, and they've agreed.

## Safety nets

- [ ] **My project has an "undo history"** (Git, or the platform's version history switched on).
  *Why: one person lost their whole app because the AI deleted it and there was no undo. (VC-02)*
- [ ] **I'm working with practice data, not the real thing.**
  *Why: an AI deleted a company's live database during a "code freeze". (VC-01)*
- [ ] **I know where my passwords and keys will be kept**, and it's not in the chat.
  *Why: leaked keys let strangers read data and spend your money. (VC-15)*
- [ ] **Spending limits are switched on** for every paid service I'll use.
  *Why: one automation ran for 11 days and cost $47,000. (VC-11)*
- [ ] **Auto-approve / "turbo" / "YOLO" modes are OFF.** The AI must ask me before running anything.
  *Why: in turbo mode, one AI wiped a whole computer drive. (VC-09)*

## Plan

- [ ] **I've written my "done means" list**: three to five sentences about what the app must do, and at least one thing it must **never** do.
  *Example: "A visitor who isn't logged in must never see the orders page."*
- [ ] **I've added the project to the team's project list** (Level 1 and above).

All ticked? Go to [Checklist B](B-every-session.md) and start your first session.
