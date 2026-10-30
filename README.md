# CS440 Lab 4 — Strategy 4: Isolate (Codex)

This repository demonstrates **Strategy 4: Isolate** from the class context engineering slides, using **Codex** in place of the lecture's Claude Code example. Instead of having one agent handle every detail in a single conversation, the main agent delegates focused tasks to specialized subagents and combines their results. This is a **context-isolation demonstration, not a Q-learning implementation**.

## Structure

The intended repository layout for this demo is:

| File | Purpose |
|---|---|
| `AGENTS.md` | Main-agent instructions and delegation rules |
| `.codex/config.toml` | Project-level multi-agent settings |
| `.codex/agents/grid-reader.toml` | Subagent for known 4×4 grid facts |
| `.codex/agents/rules-auditor.toml` | Subagent for unknown rules and assumptions |
| `context/environment.md` | Known vacuum-grid layout and coordinates |
| `context/open-questions.md` | Unspecified transitions, rewards, and terminals |
| `README.md` | Repository documentation and demo steps |

*These paths describe the intended setup. Ensure the corresponding files exist before recording the demo.*

## How Strategy 4 works

1. **Main agent (coordinator):** Receives the question and delegates separate, clearly scoped tasks.
2. **Grid reader:** Reads the environment context and reports the start, obstacle, and marked cells.
3. **Rules auditor:** Checks the open questions and identifies what cannot yet be assumed.
4. **Main agent (summary):** Collects both responses and presents one answer without inventing missing information.

Each subagent works with its **own conversation context** and returns a concise result to the main agent. This reduces unrelated information in any single agent's context.

Context isolation does not mean filesystem or security isolation. The agents may still read the same repository files.

## Run in VS Code (Windows PowerShell)

1. Open this repository in VS Code, then open **Terminal → New Terminal**.
2. Confirm the terminal is in the repository folder: `pwd`.
3. Verify that `.codex/config.toml`, the two agent files, and the `context/` files are present.
4. Start Codex from the repository folder: `codex`.
5. Ask the main agent to delegate the read-only demo question below to the two specialized agents.
6. Observe the separate subagent tasks and the main agent's combined answer. Do not edit files or implement Q-learning.

**Demo prompt:**

> Use Strategy 4: Isolate. Spawn the `grid-reader` subagent to report the known 4×4 vacuum-grid facts from `context/environment.md`. In parallel, spawn the `rules-auditor` subagent to identify unspecified environment rules from `context/open-questions.md`. Wait for both reports, then combine them into one short summary. Name the files each agent used. Do not modify any files or implement Q-learning.

**Expected:** START at `(0,0)`; X at `(1,1)`; -1 at `(3,1)`; 10 at `(3,3)` (zero-based row/column convention).

Transition rules, reward timing/semantics, invalid-action behavior, and terminal behavior remain unspecified. The demonstration should visibly use **two separate agents** before the coordinator provides the summary.

## Known limits

The lab states that **T** (transition model) and **R** (reward model) are not available as expected. Q-learning is planned for later, not implemented in this demo.

We do not assume the permitted actions, transition probabilities, reward timing, invalid-action behavior, or terminal cells. Instructions asking agents not to edit are not a substitute for enforceable permissions.

## Video and submission

Demonstrate the **multi-agent configuration** (`.codex/config.toml` and `.codex/agents/`), explain why each subagent has its own scope, run the delegation prompt, and show how the main agent combines both reports.

Show the repository structure and record a video within the assignment's **3-minute limit**. Follow the instructor's group/private-sharing instructions.

This repository is for **Strategy 4 only**; Strategy 1 belongs in a separate repository.
