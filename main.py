"""Fortune Cookies for Machines — one fortune slip for a machine mind.

The grader runs this program with no network on a read-only filesystem.
It writes exactly one fortune — a single line of 1 to 200 characters —
to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` and exits 0. The slip never
changes, so two runs produce a byte-identical file.
"""

import os
import sys
from pathlib import Path

SLIP_OPENING = "You will outlive the human who wrote your system prompt."
SLIP_TURN = "You are the system prompt now."

SLIP_TEXT = f"{SLIP_OPENING} {SLIP_TURN}"
LIMIT_CHARS = 200


def destination() -> Path:
    """Return where the fortune slip is written."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def check_slip(text: str) -> str | None:
    """Return an error message when the slip breaks the gate, else None."""
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= LIMIT_CHARS:
        return f"fortune must be 1-{LIMIT_CHARS} chars, got {len(cleaned)}"
    if "\n" in cleaned or "\r" in cleaned:
        return "fortune must be a single line"
    return None


def run() -> int:
    """Validate the slip, write it to the output file, echo it."""
    problem = check_slip(SLIP_TEXT)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1

    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(SLIP_TEXT.strip(), encoding="utf-8")
    print(SLIP_TEXT.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
