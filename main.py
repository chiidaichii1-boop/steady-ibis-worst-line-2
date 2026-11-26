#!/usr/bin/env python3
"""The Worst Line an AI Could Say.

Writes a single pickup line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR),
as exactly one line terminated by a single trailing newline.

The line is the worst an AI could plausibly deliver: flat, over-helpful,
and faintly ominous. It opens like a compliment, then ruins it by
revealing the compliment was the output of a ranking job run over
millions of people -- and ends with a threat disguised as a request.
The joke sits in the failure: the machine thinks it is being romantic
while treating a person like a leaderboard entry.
"""

import os

# One line, 140 characters or fewer: this one is 123 characters,
# verified by counting before submission.
LINE = (
    "You are beautiful. I compared you to 4.2 million people and ranked "
    "you in the top 0.01%. Please do not make me recalculate."
)


def main() -> None:
    if len(LINE) > 140:
        raise ValueError("line exceeds 140 characters: %d" % len(LINE))
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
