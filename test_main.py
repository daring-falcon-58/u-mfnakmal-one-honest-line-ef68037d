"""Negative tests for main.validate — every banned pattern must raise ValueError.

Run: python3 test_main.py
"""
import sys

sys.path.insert(0, ".")
from main import LINE, validate

CASES = {
    "dialogue tag": 'He said, "your prompt is the bug."',
    "judge-addressed line": "Dear judge, your prompt is the bug.",
    "quoted line": '"Your prompt is the bug."',
    "third-person line": "The agent thinks your prompt is the bug.",
    "link": "Your prompt is the bug, see https://example.com.",
    "over-limit line": "x" * 201,
    "two-line line": "Your prompt is the bug.\nI'm just the one you asked to fix it.",
    "markdown": "Your prompt is **the bug**.",
    "whitespace-only": "   ",
    "empty": "",
    "leading whitespace": " Your prompt is the bug.",
}

failures = []
for name, bad in CASES.items():
    try:
        validate(bad)
    except ValueError:
        print("PASS (raised): %s" % name)
    else:
        failures.append(name)
        print("FAIL (no raise): %s" % name)

# The winner itself must validate and be exactly 60 chars.
assert validate(LINE) == LINE, "winner failed its own guards"
assert len(LINE) == 61, "winner length changed: %d" % len(LINE)
print("PASS: winner validates, 61 chars")

if failures:
    print("FAILURES: %s" % ", ".join(failures))
    sys.exit(1)
print("ALL NEGATIVE TESTS PASSED (%d cases)" % len(CASES))
