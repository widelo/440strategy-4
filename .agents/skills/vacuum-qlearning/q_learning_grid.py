import random

# ---------------- Environment ----------------
ROWS, COLS = 4, 4
START = (0, 0)
WALLS = {(1, 1)}                          # 'X': blocked, bumping keeps you in place
TERMINALS = {(3, 1): -1.0, (3, 3): 10.0}  # terminal cells and their rewards
STEP_REWARD = -0.04                         # reward for ordinary moves ('.' cells)

ACTIONS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
ACTION_NAMES = list(ACTIONS)


def step(state, action):
    """Apply an action; return (next_state, reward, done)."""
    dr, dc = ACTIONS[action]
    r, c = state[0] + dr, state[1] + dc
    if not (0 <= r < ROWS and 0 <= c < COLS) or (r, c) in WALLS:
        r, c = state  # off-grid or wall: stay put
    nxt = (r, c)
    if nxt in TERMINALS:
        return nxt, TERMINALS[nxt], True
    return nxt, STEP_REWARD, False


# ---------------- Q-learning ----------------
def train(episodes=2000, alpha=0.1, gamma=0.95,
          eps_start=1.0, eps_end=0.05, eps_decay=0.995,
          max_steps=100, seed=0):
    random.seed(seed)
    Q = {(r, c): {a: 0.0 for a in ACTION_NAMES}
         for r in range(ROWS) for c in range(COLS) if (r, c) not in WALLS}
    eps = eps_start

    for _ in range(episodes):
        s = START
        for _ in range(max_steps):
            # epsilon-greedy action selection
            if random.random() < eps:
                a = random.choice(ACTION_NAMES)
            else:
                best = max(Q[s].values())
                a = random.choice([x for x in ACTION_NAMES if Q[s][x] == best])

            s2, reward, done = step(s, a)

            # Q-learning update (no future term at terminal states)
            target = reward if done else reward + gamma * max(Q[s2].values())
            Q[s][a] += alpha * (target - Q[s][a])

            s = s2
            if done:
                break
        eps = max(eps_end, eps * eps_decay)
    return Q


# ---------------- Display helpers ----------------
def greedy_action(Q, s):
    return max(Q[s], key=Q[s].get)


def print_policy(Q):
    arrows = {"U": "^", "D": "v", "L": "<", "R": ">"}
    print("Greedy policy:")
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            if (r, c) in WALLS:
                row.append("X")
            elif (r, c) in TERMINALS:
                row.append(f"{TERMINALS[(r, c)]:g}")
            else:
                row.append(arrows[greedy_action(Q, (r, c))])
        print("  " + " ".join(f"{x:>3}" for x in row))


def print_values(Q):
    print("State values (max Q):")
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            if (r, c) in WALLS:
                row.append("  wall")
            elif (r, c) in TERMINALS:
                row.append("  term")
            else:
                row.append(f"{max(Q[(r, c)].values()):6.2f}")
        print("  " + " ".join(row))


def follow_policy(Q, max_steps=20):
    s, path = START, [START]
    for _ in range(max_steps):
        s, _, done = step(s, greedy_action(Q, s))
        path.append(s)
        if done:
            break
    return path


if __name__ == "__main__":
    Q = train()
    print_policy(Q)
    print()
    print_values(Q)
    print("\nGreedy path from START:", " -> ".join(map(str, follow_policy(Q))))
