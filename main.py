#!/usr/bin/env python3
"""The 3 AM Commit Message.

Writes a single line -- the commit message an AI agent would write right
after breaking production at 3 AM -- to entry.txt inside
$ENTRY_OUTPUT_DIR (default /output). Standard library only, no network,
deterministic.
"""

import os

LINE = "fix: deployed at 3 AM with 99.9% confidence; prod is down with 100% certainty and I am still 99.9% confident"


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
