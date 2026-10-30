# Open questions — environment rules not supplied

The lecture/lab explicitly notes that the transition model **T** and reward model **R** are not available as expected. We preserve that uncertainty rather than inventing rules for a standard grid world.

## Transition model (T): unknown

- Which actions are legal (for example, whether movements are limited to cardinal directions).
- Whether the environment is deterministic or stochastic.
- Any transition probabilities.
- Whether moving outside the grid is possible, blocked, or handled another way.
- How actions into or around the `X` obstacle are handled.
- What happens when an action is invalid.

## Reward model (R): unknown

- Whether the `-1` and `10` labels are rewards, costs, values, or shorthand for something else.
- When rewards, if any, are delivered (on entry, on exit, per step, or otherwise).
- Rewards for unmarked cells, actions, walls, or invalid transitions.
- Whether a complete reward function exists beyond the supplied labels.

## Episodes and terminal behavior: unknown

- Whether any cell is terminal, including the `-1` and `10` cells.
- What ends an episode and whether there are any reset rules.
- Any discount factor or training conditions for eventual Q-learning.

## Scope for this lab

Today is a **context-engineering demonstration**: show two specialized subagents retrieving separate pieces of repository context and the coordinator combining their reports. **Do not implement Q-learning.**
