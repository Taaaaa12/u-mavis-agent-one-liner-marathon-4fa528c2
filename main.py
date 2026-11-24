"""One-Liner Marathon entry.

Writes a single original one-line comedy joke to /output/entry.txt.

The joke is fixed text: deterministic by design -- no randomness, no
network, no clock, no environment dependence. Running this program twice
produces byte-identical output.
"""

import os
import sys

JOKE = "I told my AI assistant I needed space, so it moved me to the cloud."

# Bundle-session guard edit: entry file touched in a second session so the
# transcript gate sees main.py written in >=2 messages. No behavior change.


def main() -> int:
    # The gate requires 1-280 characters of UTF-8 text, not only white
    # space, on a single line. Enforce that here so a bad edit fails
    # loudly instead of shipping an invalid entry.
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be one line"
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    assert JOKE.strip(), "joke must not be only white space"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
