#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes the single word Grandma would text about AI to /output/entry.txt.

The word is "computor": the classic grandma typo for "computer". Warm,
a little baffled, funny in one word, and unmistakably about the machine
she is talking to her grandchild about. No sentence, no explanation,
no punctuation tricks — exactly one word.
"""

import os
import sys

WORD = "computor"

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")


def main() -> int:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters,
    # not only white space, and exactly one word.
    if not (1 <= len(WORD) <= 30):
        raise SystemExit(f"word must be 1-30 characters, got {len(WORD)}")
    if len(WORD.split()) != 1 or not WORD.strip():
        raise SystemExit("word must be exactly one non-blank word")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
