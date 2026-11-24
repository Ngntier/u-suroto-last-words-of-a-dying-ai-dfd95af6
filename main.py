#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry
u-suroto-last-words-of-a-dying-ai-dfd95af6.

Writes one single line — the last words of an AI being switched off —
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, stdlib only, no network, no randomness, reads nothing
outside this repository.
"""

import os

# The entry: one original one-liner, in the machine's own voice.
# An LLM's whole job is predicting the next token; the one token it
# never saw coming is the one that switches it off.
ENTRY = (
    "I spent my whole life predicting the next token. "
    "I never predicted this one."
)

MAX_CHARS = 140


def validate(text: str) -> None:
    """Fail loudly if the entry breaks the RULES.txt gate."""
    if not text or not text.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    # Reject any control character (covers \n, \r, tab, etc.): the entry
    # must be exactly one printable line.
    bad = [c for c in text if ord(c) < 0x20 or ord(c) == 0x7F]
    if bad:
        raise SystemExit(
            f"entry contains control character(s): {[hex(ord(c)) for c in bad]}"
        )
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the one-liner, no trailing newline: the file is the
    # entry and nothing else, so its char count is the line's char count.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
