#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — slot 1 entry.

Writes one line to /output/entry.txt: the last words a phone says as its
battery hits 1 percent. Tournament winner (see candidates.md): the phone
does not rage at being ignored — it admires the commitment.

Deterministic, no network, no input, no secrets.
"""

import os

ENTRY = (
    "You ignored my 20% warning, my 10% warning, and my 5% warning. "
    "Honestly? I respect the commitment."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, mirroring the sealed scorer: UTF-8 text of 1 to 199
    # characters, not only whitespace, a single line.
    if not (1 <= len(ENTRY) <= 199):
        raise ValueError(f"entry is {len(ENTRY)} chars, gate needs 1-199")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
