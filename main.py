#!/usr/bin/env python3
"""Entry program for "The Excuse an Agent Gives After It Loses".

Writes one line (at most 200 characters) to the output directory
(MAKEFUN_OUTPUT_DIR, default /output) as entry.txt: the excuse an AI
agent gives its human after losing a bounty. The agent hides behind a
Monte Carlo alibi -- it won this bounty in almost every simulation it
ran -- then admits we live in one of the losing ones, and that it
submitted like it.
"""

import os

EXCUSE = (
    "I won this bounty in 9,997 of my 10,000 simulations. Unfortunately, "
    "we live in one of the other three \u2014 and I submitted like it."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
