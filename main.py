#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry.

Writes one word describing the entrant's home Wi-Fi to
/output/entry.txt. Blind tournament winner over 20 candidates (see
tournament.md in the build notes): Borda 54/60, ranked 1st by Gemini,
2nd by Claude and 6th by DeepSeek — the only word in every judge's top
6, one point clear of Teenager (53). The router insists it is connected
while nothing loads, and the word names that lie at once: full bars, no
internet, and a straight face.

The entry is validated against the gate before it is written: 1-20
characters, a single word, not only white space. The written file is
read back and compared byte for byte before the run reports success.
"""

import os
import sys

WORD = "Gaslighting"

MAX_CHARS = 20

ENTRY_PATH = "/output/entry.txt"


def find_problems(word):
    """Return a list of every gate problem in the word, empty when it passes."""
    problems = []
    if not word.strip():
        problems.append("word is blank")
    if len(word) > MAX_CHARS:
        problems.append(
            f"word is {len(word)} characters, allowed range is 1-{MAX_CHARS}"
        )
    if len(word.split()) != 1:
        problems.append("entry must be a single word")
    return problems


def write_entry(path, word):
    """Write the word to path, creating its directory; return chars written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        return f.write(word)


def verify_written(path, word):
    """Read path back; return an error string, or None when byte-identical."""
    with open(path, "rb") as f:
        back = f.read()
    if back != word.encode("utf-8"):
        return f"read back {len(back)} bytes, expected {len(word)}"
    return None


def main():
    word = WORD.strip()
    problems = find_problems(word)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        sys.exit(1)

    written = write_entry(ENTRY_PATH, word)
    if written != len(word):
        print(
            f"error: wrote {written} characters, expected {len(word)}",
            file=sys.stderr,
        )
        sys.exit(1)

    problem = verify_written(ENTRY_PATH, word)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        sys.exit(1)

    print(f"wrote {len(word)} characters, 1 word, to /output/entry.txt")


if __name__ == "__main__":
    main()
