---
name: vacuum-qlearning
description: Run, inspect, validate, or explain the CS440 vacuum-robot Q-learning solution. Use when asked to run the Lab 5 solution, check the learned policy or path, explain the living reward, discount factor, learning rate, or epsilon, or verify that the result matches the repository's documented environment and implementation assumptions.
---

# Vacuum Q-learning workflow

Use this skill for the CS440 vacuum-robot Lab 5 workflow.

1. Read `context/environment.md` first. Treat it as the source of the supplied grid facts.
2. Read `context/hyperparameters.md` if it exists. Report the selected living reward, discount factor, learning rate, and epsilon exactly as written. If the file does not exist or a value is missing, say so instead of inventing a value.
3. Read the repository `README.md` to find the documented command for running the solution.
4. Before running anything, distinguish between:
   - facts supplied by the assignment, and
   - implementation choices made by the team because T and R were not fully specified.
5. Run the solution using the command documented in the README. Do not substitute a different algorithm or silently change hyperparameters.
6. Inspect the output for the learned policy or path and the final outcome. Verify that the reported behavior is consistent with the documented grid and implementation choices.
7. If the solution fails, report the failure and the relevant output. Do not fabricate a successful run.
8. When explaining the result, use this compact format:
   - **Hyperparameters:** living reward, discount factor, learning rate, epsilon.
   - **Environment:** start, obstacle, negative cell, positive goal.
   - **Result:** learned policy/path and whether the goal was reached.
   - **Assumptions:** any team-selected transition, reward, or terminal rules needed to make the environment runnable.

Keep the explanation concise enough to support a short class demo. Do not modify project files unless the user explicitly asks for changes.
