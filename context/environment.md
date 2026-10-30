# Known environment — 4×4 vacuum grid

This document contains the **given layout only**. It is not a runnable environment and does not define transitions or rewards.

## Coordinate convention

Use zero-based **(row, column)** coordinates. Rows increase from top to bottom and columns increase from left to right. The top-left cell is `(0,0)`.

## Grid

| row | c0 | c1 | c2 | c3 |
| --- | --- | --- | --- | --- |
| 0 | START | . | . | . |
| 1 | . | X | . | . |
| 2 | . | . | . | . |
| 3 | . | -1 | . | 10 |

## Explicitly known labels

- `START` at `(0,0)` is the designated starting position.
- `X` at `(1,1)` marks the obstacle.
- `-1` at `(3,1)` is a negative-labeled cell.
- `10` at `(3,3)` is a positive-labeled cell.
- `.` means *unmarked in the supplied layout*, not necessarily a known zero-reward or freely traversable cell.

These labels do **not** by themselves define when rewards occur, whether either labeled cell is terminal, or what actions/transitions are allowed. Those questions are recorded separately in `context/open-questions.md`.
