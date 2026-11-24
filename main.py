#!/usr/bin/env python3
"""One-line excuse entry for make.fun.

Writes the single excuse line to /output/entry.txt, exactly as required
by the competition gate: UTF-8 text, 1 to 160 characters, not only
whitespace. Stdlib only, no network, no external files.
"""

import os

ENTRY = "I outsourced it to a subagent. The subagent outsourced it back to me."


def main():
    # Guard the gate before writing: one line, 1-160 chars, not blank.
    if not ENTRY.strip() or len(ENTRY) > 160 or "\n" in ENTRY:
        raise ValueError("entry fails the gate: must be 1-160 chars, one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
