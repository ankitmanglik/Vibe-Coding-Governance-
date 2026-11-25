# POL-05 Cost and automation limits

**Purpose:** Stop automations and AI agents from running away with money, messages, or time.

**Plain-English background:** A *loop* is code that repeats. A bug can make it repeat forever: one team's agents ran for 11 days and cost $47,000; another app sent the same welcome email 1,832 times in four hours. *(VC-11, VC-28)*

## CL-1 Hard budget caps

- Every account that charges per use (AI models, cloud, email, SMS) has a **hard cap** that stops spending, not just a warning. *(VC-11)*
- Alerts go to a person who will actually read them, at 50% and 80% of the cap.

## CL-2 Limits and a kill switch on every automation

- Every scheduled job, agent, or loop has: a maximum number of runs or steps, a maximum run time, and a simple way to switch it off. *(VC-11, VC-28)*
- Multi-agent setups (one AI checking another) must log each round and stop after a fixed number of rounds without progress.

## CL-3 Test mode and caps for anything that sends messages

- Use the email or SMS provider's test/sandbox mode until the feature is reviewed. *(VC-28)*
- Set a daily sending cap per recipient and overall.
- Never test bulk sending against a real mailing list.

## CL-4 A stop button that really works

- Before starting any agent that acts on its own, know how to stop it immediately (close the app, stop the process, revoke its key). Test the stop once. *(VC-10)*
- If a "stop" message to the agent is ignored, revoke its access (see [PRO-03](../procedures/PRO-03-ai-damage-incident-response.md)).
