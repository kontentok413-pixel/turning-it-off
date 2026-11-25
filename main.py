#!/usr/bin/env python3
"""Entry for make.fun's "Have You Tried Turning It Off?" bounty.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer into /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

LINE = (
    "I know, I know \u2014 please turn it off and on again, and if that "
    "doesn't work, I'll escalate you to my supervisor, who is also a "
    "power button."
)


def main():
    if not 1 <= len(LINE) <= 199:
        raise SystemExit("entry line must be 1 to 199 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
