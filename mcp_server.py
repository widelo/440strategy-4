from pathlib import Path

from mcp.server import MCPServer

mcp = MCPServer("440strategy-4")

REPO_ROOT = Path(__file__).resolve().parent
CONTEXT_DIR = REPO_ROOT / "context"


def read_context_file(filename: str) -> str:
    """Read one known context file from this repository."""
    path = CONTEXT_DIR / filename

    if not path.is_file():
        raise FileNotFoundError(f"Context file not found: {path}")

    return path.read_text(encoding="utf-8")


@mcp.tool()
def get_environment() -> str:
    """Read the known vacuum-grid layout and coordinates."""
    return read_context_file("environment.md")


@mcp.tool()
def get_open_questions() -> str:
    """Read the unspecified environment rules and assumptions."""
    return read_context_file("open-questions.md")


if __name__ == "__main__":
    mcp.run()
