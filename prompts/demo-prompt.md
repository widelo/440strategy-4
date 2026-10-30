# Strategy 4 — ready-to-paste Codex demo prompt

Use **Strategy 4: Isolate**. Spawn the `grid_reader` subagent to report the known 4×4 vacuum-grid facts **only** from `context/environment.md`. Spawn the `rules_auditor` subagent to report the unspecified environment rules **only** from `context/open-questions.md`.

Run the two tasks separately, preferably in parallel. Wait for both to finish. Then combine their reports into one concise answer with these headings: **Known grid**, **Still unknown**, and **Delegation evidence**. Under delegation evidence, name both subagents and the file each consulted.

Do not modify any files, infer missing environment behavior, or implement Q-learning. If subagent delegation is unavailable, say so rather than pretending it happened.
