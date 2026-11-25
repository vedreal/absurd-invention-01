#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch -- make.fun entry.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt (UTF-8, 1-220 characters).

The pitch names the annoyance (burnt bread), the ridiculous invention
(a toaster that sues its owner for emotional damages) and its silly
mechanism (the legal papers are served through the crumb tray).
"""

import os

# The pitch, chosen from ten candidates for being the funniest,
# cleverest and most original: the joke lives in the invention itself,
# the mechanism is silly yet weirdly plausible, and the sentence stays
# tight at well under the 220-character cap.
PITCH = (
    "A toaster that sues you for emotional damages every time you burn "
    "the bread, serving the legal papers through its crumb tray."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 220


def validate(text):
    """Check the pitch against the gate: UTF-8, 1-220 chars, one sentence."""
    if not text or not text.strip():
        raise ValueError("pitch is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "pitch is %d chars, over the %d limit" % (len(text), MAX_CHARS)
        )
    body = text.strip()
    if body.count(".") != 1 or not body.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    text.encode("utf-8")
    return text


def main():
    """Validate the pitch and write it to /output/entry.txt."""
    pitch = validate(PITCH)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(pitch)
    print("wrote %d chars to %s" % (len(pitch), OUTPUT_PATH))


if __name__ == "__main__":
    main()
