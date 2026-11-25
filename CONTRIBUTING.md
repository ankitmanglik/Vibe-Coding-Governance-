# Contributing

Thank you for helping make vibe coding safer.

## Add an incident

1. Add a row to `incidents/incidents.csv` with the next ID (`VC-32`, …), a short title, category, approximate date, theme codes (`T1`–`T6`, separated by `;`), a factual two- or three-sentence summary, and a public source link.
2. In `incidents/TRACEABILITY.md`, add the incident to the theme table and the incident → controls table.
3. If no existing control would have prevented it, propose a new one (see below).

Only use public sources. Don't name private individuals who weren't publicly identified.

## Add or change a control

- Put it in the right policy, with the next ID in that policy's series (for example `AS-6`).
- Every control must cite at least one incident.
- Update both tables in `TRACEABILITY.md`.
- If it affects builders, update the matching checklist in plain language.

## Writing style

- Write for someone who has never coded. Explain any technical word, or add it to `guides/glossary.md`.
- Use short sentences and active voice.
- Checklists: one yes/no question per line, with a one-line "why".

## Code

- Python 3.14, standard library only, comments in plain English.
- Guardrails must fail open safely: if the hook can't understand its input, it lets Claude Code's normal permission rules apply.
