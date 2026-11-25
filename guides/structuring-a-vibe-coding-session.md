# How to run a vibe coding session (for non-technical builders)

A good session is short, has one goal, and ends with something saved that works. This guide gives you a repeatable shape to follow. It works with any AI tool: Claude, Cursor, Lovable, Replit, and others.

> **Tip:** In Claude, you can say *"Use the vibe-session-coach skill"* and it will walk you through these phases one by one.

## The shape of a session

```
 1. PREPARE  →  2. PLAN  →  3. BUILD (small loops)  →  4. CHECK  →  5. SAVE & CLOSE
   5 min        5–10 min       repeat 3–6 times           10 min        5 min
```

Aim for **60–90 minutes**. Longer sessions are where AIs forget rules and make sweeping changes. *(VC-10, VC-30)*

---

## Phase 1: Prepare (5 minutes)

1. Run [Checklist B, "At the start"](../checklists/B-every-session.md).
2. **Save a checkpoint** of where things are now.
3. **Start a fresh chat** and paste in your *session starter* (below).

### Session starter (copy and fill in)

```
I'm a non-technical builder. Please explain things in plain language.

Project: [one sentence about what it is]
Risk level: [0 / 1 / 2 / 3]
Today's ONE goal: [one small, specific thing]

Rules for this session:
- Ask me before deleting, moving, or overwriting any file, and list exactly what's affected.
- Never touch real/production data. We are working on the practice copy only.
- Never ask me to paste passwords or keys into the chat. Tell me where to put them instead.
- Make one small change at a time and tell me how to check it worked.
- If you're unsure about something, say so. Don't guess or make up data.
- Don't install new packages without telling me what they are and why.

Before writing any code, tell me your plan in plain words and wait for my OK.
```

## Phase 2: Plan (5–10 minutes)

1. **Let the AI explain its plan** before it builds anything. Read it.
2. **Ask these three questions:**
   - "Which files will you change?"
   - "Could this break anything that already works?"
   - "How will I check it worked?"
3. **Break it down.** If the plan has more than five steps, ask it to split the goal and do only the first part today.
4. **Add a "never" rule** for today's change, for example *"a logged-out visitor must never see this page"*.

## Phase 3: Build in small loops (repeat)

Each loop looks like this:

```
  Ask for ONE step  →  Read what it wants to do  →  Approve or say no
        ↑                                                  ↓
  Save checkpoint  ←  It works?  ←  Try it yourself  ←  It makes the change
```

- **Read every request to run a command.** Use the table in [Checklist B](../checklists/B-every-session.md). When in doubt, say *"Explain what this does in plain words before I approve."*
- **If it works:** save a checkpoint with a note ("added contact form").
- **If it doesn't work:** describe what you see, not what you think the cause is. *"When I click Send, nothing happens and the page goes blank"* is better than *"fix the bug"*.
- **If the same problem comes back three times:** stop the loop. Go back to your last checkpoint, and either try a different approach or ask a person. *(VC-06, VC-29)*

## Phase 4: Check (10 minutes)

1. **Try your "done means" list** by hand. Does everything still work, including things you didn't touch today?
2. **Ask the AI for a review**: *"Review today's changes for security problems: exposed keys, missing login checks, missing data access rules, and anything that could run in a loop. Explain in plain words."*
3. **Don't take "all good" at face value.** Ask: *"How did you check that? Show me."* *(VC-28)*
4. If the project is being shared, run [Checklist C](../checklists/C-before-you-share.md).

## Phase 5: Save and close (5 minutes)

1. Save a final checkpoint.
2. Back it up (push to GitHub, or whatever your platform uses).
3. **Ask the AI for a handover note**: *"Write a short summary of what we did today, what's left, and anything I should know, so I can paste it into my next session."* Save this note in your project (for example, in a `NOTES.md` file).
4. Close the chat. Next time, start fresh with your session starter plus the handover note.

---

## Red flags: stop the session if...

- The AI wants to delete, reset, or "clean up" things you didn't ask about.
- It asks for a password or key in the chat.
- It says something is impossible to undo. *(VC-01)*
- It keeps changing files unrelated to your request.
- You've lost track of what it's doing.

Stopping is always allowed. Your last checkpoint is waiting for you.
