#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line (200 characters or fewer) to /output/entry.txt.
Deterministic, no network, no input, no randomness.
"""

import os
import sys

LINE = "I asked my AI assistant to tell me a joke, and it said 'your code' — I've never been roasted by something I pay to obey me."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(
            f"entry must be 1-{MAX_CHARS} characters, got {len(LINE)}",
            file=sys.stderr,
        )
        raise SystemExit(1)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
