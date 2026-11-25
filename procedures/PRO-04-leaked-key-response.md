# PRO-04 When a secret key leaks

**When:** A key, token, or password was pasted into chat, committed to a repository, put in browser code, posted publicly, or you just aren't sure.
**Who:** The builder, right away. Tell the security contact.
**Controls:** AS-1 to AS-5

Assume someone already has it. Bots scan public code for keys within minutes.

1. **Replace the key.** In the service's settings, create a new key and delete or revoke the old one. *This is the step that matters.* Deleting the file or message does not un-leak the key.
2. **Update your app** to use the new key, stored in the secret manager or `.env`, not in code.
3. **Check for misuse.** Look at the service's usage, billing, and logs since the leak. Look for unexpected charges, data downloads, or new users. *(VC-15, VC-20)*
4. **Clean up the history** (with your reviewer). The key stays in Git history even after deletion; scrubbing it is cleanup, not protection.
5. **Tell the security contact** what leaked, where, for how long, and what you found in step 3.
6. **Prevent a repeat.** Check `.gitignore`, turn on secret scanning and push protection, and install the [guardrail hook](../guardrails/).
