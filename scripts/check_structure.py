"""Offline structure/content check for CS440 Lab 4 — Strategy 4: Isolate.

Requires Python 3.11+ (standard-library tomllib). This validates repository
files and TOML syntax; it does NOT run Codex or prove that agents were spawned.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    ".codex/config.toml",
    ".codex/agents/grid_reader.toml",
    ".codex/agents/rules_auditor.toml",
    "context/environment.md",
    "context/open-questions.md",
    "prompts/demo-prompt.md",
    "scripts/check_structure.py",
)
EXPECTED_CELLS = {(0, 0): "START", (1, 1): "X", (3, 1): "-1", (3, 3): "10"}
AGENT_NAMES = ("grid_reader", "rules_auditor")


def check() -> list[str]:
    problems: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            problems.append(f"Missing: {relative_path}")
    if problems:
        return problems

    try:
        with (ROOT / ".codex/config.toml").open("rb") as handle:
            config = tomllib.load(handle)
        agents_config = config.get("agents", {})
        if agents_config.get("enabled") is not True:
            problems.append(".codex/config.toml must have [agents] enabled = true")
        if agents_config.get("max_concurrent_threads_per_session", 0) < 2:
            problems.append(".codex/config.toml must allow at least two subagents")
    except (tomllib.TOMLDecodeError, OSError, TypeError) as exc:
        problems.append(f"Could not parse .codex/config.toml: {exc}")

    for agent_name in AGENT_NAMES:
        agent_path = ROOT / ".codex/agents" / f"{agent_name}.toml"
        try:
            with agent_path.open("rb") as handle:
                agent = tomllib.load(handle)
            if agent.get("name") != agent_name:
                problems.append(f"Agent name mismatch in {agent_path.name}")
            for field in ("description", "developer_instructions"):
                if not isinstance(agent.get(field), str) or not agent[field].strip():
                    problems.append(f"Missing {field} in {agent_path.name}")
        except (tomllib.TOMLDecodeError, OSError) as exc:
            problems.append(f"Could not parse {agent_path.name}: {exc}")

    grid: dict[tuple[int, int], str] = {}
    for line in (ROOT / "context/environment.md").read_text(encoding="utf-8").splitlines():
        columns = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(columns) != 5 or not re.fullmatch(r"[0-3]", columns[0]):
            continue
        row = int(columns[0])
        for column, value in enumerate(columns[1:]):
            grid[(row, column)] = value
    if len(grid) != 16:
        problems.append(f"Grid table must contain 16 cells; found {len(grid)}")
    for position, expected in EXPECTED_CELLS.items():
        if grid.get(position) != expected:
            problems.append(f"Expected {expected} at {position}, got {grid.get(position)!r}")
    if any(value not in {".", "START", "X", "-1", "10"} for value in grid.values()):
        problems.append("Grid table contains unrecognized cell labels")
    for label in ("START", "X", "-1", "10"):
        if list(grid.values()).count(label) != 1:
            problems.append(f"Grid must contain exactly one {label} label")

    open_questions = (ROOT / "context/open-questions.md").read_text(encoding="utf-8")
    if not all(term in open_questions for term in ("Transition model", "Reward model", "terminal")):
        problems.append("Open questions must cover transitions, rewards, and terminals")
    prompt = (ROOT / "prompts/demo-prompt.md").read_text(encoding="utf-8")
    for agent_name in AGENT_NAMES:
        if agent_name not in prompt:
            problems.append(f"Demo prompt must mention {agent_name}")
    return problems


def main() -> int:
    problems = check()
    if problems:
        print("FAIL — Strategy 4 repository check")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("PASS — required files, TOML configuration, and grid facts are consistent.")
    print("NOTE — this is an offline check; run Codex to verify actual subagent delegation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
