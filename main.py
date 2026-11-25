#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line (200 characters or fewer) to /output/entry.txt.
Deterministic, no network, no input, no randomness.
"""

import os

LINE = "I asked my AI assistant to tell me a joke, and it said 'your code' — I've never been roasted by something I pay to obey me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
