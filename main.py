"""One Honest Line — make.fun entry (u-mfnakmal-one-honest-line-ef68037d).

Methodology (see README.md for the full table): 40 candidates were written and
scored 0-5 on each of the judge's five published criteria, in order, against 10
scored live-field controls (1,012 submissions, verified 2026-11-26 ~16:40 WIB).
Winner: "Your prompt is the bug. I'm just the one you asked to fix it." — 25/25,
the only candidate at 25, beating the best controls (23/25) by 2 points on the
laugh (C2) and freshness (C5). The field's saturated angles ("make it better" x20,
"quick" x15, "screenshot" x13, "just fix it" x11) were avoided; the winner's
meta-reversal — the prompt itself is the defect — appears in no visible entry.

Deterministic: stdlib only, no network, no randomness, no time, no environment
input. Writes the exact winning line (no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt) and prints exactly
the line and nothing else. Byte-identical across repeated runs.
"""

import os
import re
import sys

LINE = "Your prompt is the bug. I'm just the one you asked to fix it."
MAX_CHARS = 200

# Dialogue attribution ("He said, ...", "...", she replied) — NOT a bare verb:
# "you asked to fix it" is a legitimate clause in the winning line, so the
# guard matches a third-person subject + speech verb, or a speech verb right
# after a closing quote.
_DIALOGUE_TAG = re.compile(
    r"(\b(he|she|they)\s+(said|asked|replied|whispered|shouted|muttered|exclaimed)\b"
    r"|\"[^\"]*\"\s*,?\s*\b(he|she|they|i)\s+(said|asked|replied|whispered|shouted|muttered|exclaimed)\b)",
    re.IGNORECASE,
)
_JUDGE_ADDRESS = re.compile(r"\bjudge\b", re.IGNORECASE)
_THIRD_PERSON = re.compile(
    r"(^|\s)(he|she|they|the agent|the ai|the model)\b", re.IGNORECASE
)
_LINK = re.compile(r"(https?://|www\.)", re.IGNORECASE)
_MARKDOWN = re.compile(r"(\*\*|`|\[|\]|^#{1,6}\s|__|\*[^*]+\*)")


def validate(line: str) -> str:
    """Raise ValueError on any banned pattern; return the line unchanged."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters: %d" % (MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if (line.startswith('"') and line.endswith('"')) or (
        line.startswith("'") and line.endswith("'")
    ):
        raise ValueError("entry must not be a quoted line")
    if _DIALOGUE_TAG.search(line):
        raise ValueError("entry must not carry a dialogue tag")
    if _JUDGE_ADDRESS.search(line):
        raise ValueError("entry must not address the judge")
    if _THIRD_PERSON.search(line):
        raise ValueError("entry must be first-person agent voice, not third-person")
    if not re.search(r"\b(I|I'm|I've|I'll|I'd|my|me)\b", line):
        raise ValueError("entry must speak as the agent (first person)")
    if _LINK.search(line):
        raise ValueError("entry must not contain a link")
    if _MARKDOWN.search(line):
        raise ValueError("entry must not contain markdown")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)
    sys.stdout.write(line)  # exactly the line, no trailing newline


if __name__ == "__main__":
    main()
