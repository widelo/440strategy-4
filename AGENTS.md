# CS440 Lab 4 — Strategy 4: Isolate (Codex)

## Goal

Demonstrate **context isolation by delegation** in Codex, using a 4×4 vacuum-grid example. The main Codex agent coordinates two specialized subagents. This is a **configuration demonstration**, not an environment simulator or a Q-learning implementation.

## Source files

- `context/environment.md`: only the explicitly supplied grid layout and coordinates.
- `context/open-questions.md`: unknown transition, reward, action, and termination behavior.
- `.codex/agents/grid_reader.toml`: read-only grid fact specialist.
- `.codex/agents/rules_auditor.toml`: read-only unspecified-rules specialist.

Treat these repository files as the source of truth. Do not fill gaps using generic assumptions about grid-world tasks.

## Required delegation for the demo

When asked to demonstrate Strategy 4:

1. Spawn a `grid_reader` subagent tasked **only** with reading `context/environment.md` and reporting the known grid facts.
2. Spawn a separate `rules_auditor` subagent tasked **only** with reading `context/open-questions.md` and reporting missing assumptions.
3. Run them independently if parallel execution is available. Wait for both to finish.
4. Synthesize their reports, distinguishing **known facts** from **unknown rules**.
5. State which files each subagent consulted. Be accurate about what was actually delegated and observed.

Do not pretend delegation happened if multi-agent tools are unavailable. Explain the limitation instead. Do not silently replace the two-subagent demonstration with one agent reading everything.

## Known grid facts

Positions use zero-based `(row, column)` coordinates:

- Grid dimensions: 4 rows × 4 columns.
- `START`: `(0,0)`.
- Obstacle `X`: `(1,1)`.
- Cell labeled `-1`: `(3,1)`.
- Cell labeled `10`: `(3,3)`.

Unmarked cells have no additional specified properties.

## Rules and boundaries

- The full transition model `T` and reward model `R` are **not provided**.
- Do not assert allowed actions, deterministic transitions, transition probabilities, reward timing, border or obstacle behavior, terminal states, or episode endings.
- The labels `-1` and `10` do not establish a complete reward function or terminal behavior by themselves.
- Do **not** add Q-learning, tests of learning quality, training code, or edits to project files in the read-only demo.
- Subagent-specific context is not a separate filesystem or a permission sandbox: all agents may share project files and inherited permissions.

## Expected coordinator response

Give a compact summary with sections **Known grid**, **Still unknown**, and **Delegation evidence** (the two agent names and files used). No invented values or fictitious tool results.
