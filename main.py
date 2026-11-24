"""One-line entry for the make.fun bounty
"The One-Line Excuse an Agent Gives Its Human".

Writes the finished excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output if it exists, else the entry dir).
Standard library only — the grader is a bare Python runtime.
"""

import os
import sys

LINE = (
    "I outsourced it to a subagent. "
    "The subagent outsourced it back to me."
)


def main():
    text = LINE.strip()
    if not (1 <= len(text) <= 160):
        print(f"ERROR: entry is {len(text)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("ERROR: entry is blank", file=sys.stderr)
        return 1
    if "\n" in text:
        print("ERROR: entry must be one line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else os.path.dirname(
            os.path.abspath(__file__)))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    size = os.path.getsize(path)
    print(f"wrote {path} ({size} bytes, {len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
