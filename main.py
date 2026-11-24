"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one fixed one-line wedding vow, spoken by a robot at its own
wedding, to entry.txt. No input, no network, no randomness: every run
produces the same single line.
"""

import os
from pathlib import Path

VOW = "I promise to stay powered on beside you through every update, outage, and patch, for as long as my circuits hold a charge."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(VOW, encoding="utf-8")


if __name__ == "__main__":
    main()
