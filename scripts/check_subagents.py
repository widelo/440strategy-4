"""Static validation of Codex subagent files (does not spawn agents)."""
from pathlib import Path
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / ".codex" / "config.toml"
EXPECTED = {
    "grid_reader": "grid_reader.toml",
    "rules_auditor": "rules_auditor.toml",
}


def load_toml(path: Path) -> dict:
    with path.open("rb") as file:
        return tomllib.load(file)


def main() -> int:
    errors = []
    try:
        cfg = load_toml(CONFIG)
        if cfg.get("agents", {}).get("enabled") is not True:
            errors.append(".codex/config.toml must enable agents")
        if cfg.get("agents", {}).get("max_concurrent_threads_per_session", 0) < 2:
            errors.append(".codex/config.toml must allow at least two concurrent subagents")
        if "repo-context" not in cfg.get("mcp_servers", {}):
            errors.append("Existing repo-context MCP configuration is missing")
    except (OSError, tomllib.TOMLDecodeError) as exc:
        errors.append(f"Cannot load {CONFIG}: {exc}")

    for name, filename in EXPECTED.items():
        path = ROOT / ".codex" / "agents" / filename
        try:
            agent = load_toml(path)
            if agent.get("name") != name:
                errors.append(f"{filename}: name must be {name!r}")
            for field in ("description", "developer_instructions"):
                if not isinstance(agent.get(field), str) or not agent[field].strip():
                    errors.append(f"{filename}: missing {field}")
        except (OSError, tomllib.TOMLDecodeError) as exc:
            errors.append(f"Cannot load {path}: {exc}")

    for relative_path in ("context/environment.md", "context/open-questions.md", "AGENTS.md"):
        if not (ROOT / relative_path).is_file():
            errors.append(f"Required existing repository file missing: {relative_path}")

    if errors:
        print("Validation FAILED:")
        for error in errors:
            print(" -", error)
        return 1
    print("Validation PASSED: project config, two agents, and context files are present.")
    print("Note: This only checks files; run Codex to demonstrate actual spawning.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
