# Checklist C: Before anyone else uses it

You don't need to know how to code to do these checks. You need two web browsers (or one normal window and one private/incognito window) and two test accounts.

For **Level 2 and 3** projects, your technical reviewer must also complete the [full security check](../procedures/PRO-02-pre-launch-security-check.md). This list is your part.

## Can strangers get in?

- [ ] **The "stranger test".** Open a private/incognito window (not logged in). Paste in the web address of every page, especially private ones. **You should see a login screen, not data.**
  *Why: thousands of AI-built apps let anyone see everything. (VC-03, VC-21)*
- [ ] **The "neighbour test".** Make two test accounts, A and B. Logged in as B, try to open A's pages. If the web address contains a number or ID, change it. **B must not see A's stuff.**
  *Why: one app let anonymous visitors in while blocking real users: 18,697 records exposed. (VC-16)*
- [ ] **The "wrong code test".** Type a wrong password or wrong verification code. **The message should just say it's wrong**, and never show the right one.
  *Why: one login screen leaked the real code when you typed a wrong one. (VC-28)*
- [ ] **The "free lunch test".** If anything is paid, can you reach it without paying (for example, by going straight to its web address)? **You shouldn't be able to.** *(VC-20)*

## Are secrets hidden?

- [ ] **Ask the AI:** "List every password, key, or token this project uses and tell me exactly where each one is stored." **None should be written directly in the code.**
- [ ] **Ask the AI:** "Is any secret key visible in the browser? Show me how you checked."
- [ ] **Ask your reviewer** to run a secret scanner (Level 2+).

## Can it run away?

- [ ] **Anything automatic** (scheduled jobs, emails, agents) has a limit on how many times it can run, and an off switch I know how to use.
- [ ] **Emails were tested only to my own address**, and there's a daily sending limit.
- [ ] **Spending limits are on** for every paid service.

## Can we recover?

- [ ] **The latest version is saved and backed up** outside my laptop.
- [ ] **For apps with a database:** a backup exists and someone has tried restoring it once.

## Sign-off

- [ ] Level 0–1: I've done all of the above.
- [ ] Level 2–3: my reviewer has signed the [security check](../procedures/PRO-02-pre-launch-security-check.md).
