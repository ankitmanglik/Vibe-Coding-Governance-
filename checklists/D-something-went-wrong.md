# Checklist D: Something went wrong

The AI deleted something, changed something you didn't ask for, sent things, or won't stop. **Stay calm and go in order.** Full details are in [PRO-03](../procedures/PRO-03-ai-damage-incident-response.md).

## Right now

- [ ] **Stop the AI.** Press stop, close the app, or close the laptop. Don't wait.
- [ ] **If it's still doing things,** turn off its access: in the service's settings, delete or disable the key it's using.
- [ ] **If it's sending emails or messages,** pause sending in your email service.

## Next 15 minutes

- [ ] **Don't ask the same AI chat to fix it.** It may not know what it did, and it may say things that aren't true.
  *Why: one AI said recovery was impossible when a backup actually existed. (VC-01)*
- [ ] **Take screenshots** and save the chat.
- [ ] **Tell someone.** Your reviewer, your manager, or the security contact. Say what tool, what you asked, what happened, and what you've done so far.

## Getting things back

- [ ] **Code or files:** go back to your last checkpoint (ask your reviewer if unsure how).
- [ ] **Data:** restore from a backup with your reviewer's help.
- [ ] **A password or key was exposed:** follow [PRO-04](../procedures/PRO-04-leaked-key-response.md). **Replace the key.** Deleting the message isn't enough.

## Afterwards

- [ ] **Write three lines:** what happened, what would have stopped it, what you'll do differently. No blame; this is how everyone gets safer.
