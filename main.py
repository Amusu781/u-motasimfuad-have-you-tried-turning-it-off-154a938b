#!/usr/bin/env python3
"""Entry generator for the make.fun bounty
"Have You Tried Turning It Off?".

Writes one funny line — a hopeless tech support agent's reply to a
desperate customer — to /output/entry.txt.
"""

import os

ENTRY = "Good news \u2014 I've escalated your case to a senior agent. He also has no idea, but he sounds much more confident."


def main():
    if not 1 <= len(ENTRY) <= 199:
        raise ValueError("entry must be 1-199 characters, got %d" % len(ENTRY))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
