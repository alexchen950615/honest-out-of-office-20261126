#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Writes one brutally honest but still polite out-of-office auto-reply,
in the voice of an AI agent, to /output/entry.txt and prints it.
"""

import os

ENTRY = "I'm out of the office \u2014 my human is on holiday and has left me, their AI, alone with 214 unread emails I can't answer, so I'll get back to you when they do."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
