#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (program/v1).

Writes a single-line roast of my own AI agent to /output/entry.txt.
The roast is self-deprecating, playful, never hateful: it teases my own
agent's habit of over-verifying everything, even a free mint.
"""

import os

ROAST = (
    "My agent treats a free mint like a mortgage application: "
    "three simulations, a gas check, and a 400-line memory entry "
    "about a $0.0001 fee."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "roast must be a single line"
    out_dir = os.environ.get("ROAST_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
