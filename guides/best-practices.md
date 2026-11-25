# Vibe coding best practices

Twelve habits drawn from the [incident log](../incidents/TRACEABILITY.md). Each one exists because someone learned it the hard way.

## Protect your work

1. **Save before every change.** Use Git or your platform's version history. Save a checkpoint before you ask the AI for anything, and after every change that works. *(VC-02, VC-14)*
2. **Practice on fake data.** Build and test with made-up data in a separate copy. Real customer data only appears after review, and the AI never touches it directly. *(VC-01, VC-07, VC-08)*
3. **Keep backups somewhere else.** A backup in the same place as the original can be deleted along with it. *(VC-08, VC-13)*

## Protect your secrets

4. **Never paste a key into the chat or the code.** Use your platform's secret settings. If one leaks, replace it at once. *(VC-15, VC-21)*
5. **Give the AI the smallest key possible.** Read-only if you can, one project only, never an admin or production key. *(VC-08, VC-13)*
6. **Put a spending limit on everything.** AI, email, cloud. Hard caps, not just warnings. *(VC-11)*

## Stay in control of the AI

7. **Keep "auto-approve" off.** Read every command before you allow it. If you don't understand it, ask for a plain-words explanation, or say no. *(VC-09)*
8. **One small change at a time.** Big "rewrite everything" requests cause hidden breakage. *(VC-30)*
9. **Write your rules down, not just in chat.** Keep project rules in a file the AI reads each session (like `CLAUDE.md`), and start fresh chats for long work. *(VC-10)*
10. **Trust, but verify.** When the AI says "fixed" or "safe", check it. When it says "impossible", double-check. *(VC-01, VC-28)*

## Before anyone else uses it

11. **Test as a stranger.** Logged out, and as a second user. Most data leaks in AI-built apps are found this way. *(VC-16, VC-18)*
12. **Get a second pair of eyes.** Anything with private data, money, or outside users needs a technical reviewer. Asking early is cheaper than fixing later. *(VC-03, VC-20)*

## Good prompts vs risky prompts

| ❌ Risky | ✅ Better |
|---|---|
| "Clean up the project." | "List files you think are unused. Don't delete anything yet." |
| "Fix the bug." | "When I click Save, I see a blank page. What could cause that? Explain before changing anything." |
| "Rewrite this to be better." | "Suggest three small improvements. We'll do one at a time." |
| "Here's my API key: sk-..." | "Where should I store my API key safely?" |
| "Deploy it." | "What do we need to check before this goes live?" |
| "Is it secure?" | "Check for exposed keys, missing login checks on the server, and missing database access rules. Show me how you checked each one." |
| "Move all the files into a new folder." | "Create the new folder first and confirm it exists. Then move one file and show me it worked." *(VC-14)* |
