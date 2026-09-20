#!/usr/bin/env python3
"""
check_proposal.py
------------------
Checks a drafted proposal against the platform norms and anti-patterns
defined in skills/proposal-writer/SKILL.md, so a draft can be validated
before it's sent instead of trusting the model got it right.

This is plain Python with no dependencies and no API calls — it's a
mechanical check (length, banned phrases), not a quality judgment. It
catches the easy mistakes; it does not replace reading your own draft.

Usage:
    python lib/check_proposal.py --platform upwork proposal.txt
    python lib/check_proposal.py --platform fiverr < proposal.txt
    echo "some proposal text" | python lib/check_proposal.py --platform freelancer
"""

import argparse
import re
import sys

# Word/char targets per platform, from skills/proposal-writer/SKILL.md.
# (word_min, word_max) — Fiverr buyer requests are short, Upwork mid-length.
PLATFORM_LIMITS = {
    "upwork": {"word_min": 150, "word_max": 300},
    "fiverr": {"word_min": 50, "word_max": 120},
    "freelancer": {"word_min": 80, "word_max": 250},
    "generic": {"word_min": 100, "word_max": 300},
}

# Phrases that flag a proposal as templated/copy-paste. Case-insensitive
# substring match. Sourced from skills/proposal-writer/SKILL.md anti-patterns.
BANNED_PHRASES = [
    "i have read your job posting and i am very interested",
    "dear sir/madam",
    "dear sir or madam",
    "to whom it may concern",
    "i am excited to apply",
    "your project sounds amazing",
    "just following up",
    "i've reached out several times",
    "hardworking, detail-oriented",
    "results-driven professional",
    "let me know if interested",
]


def count_words(text: str) -> int:
    return len(text.split())


def find_banned_phrases(text: str) -> list:
    lowered = text.lower()
    return [phrase for phrase in BANNED_PHRASES if phrase in lowered]


def count_exclamations(text: str) -> int:
    return text.count("!")


def check(text: str, platform: str) -> dict:
    limits = PLATFORM_LIMITS[platform]
    word_count = count_words(text)
    banned = find_banned_phrases(text)
    exclamations = count_exclamations(text)

    issues = []

    if word_count < limits["word_min"]:
        issues.append(
            f"Too short for {platform}: {word_count} words "
            f"(expected {limits['word_min']}-{limits['word_max']})"
        )
    elif word_count > limits["word_max"]:
        issues.append(
            f"Too long for {platform}: {word_count} words "
            f"(expected {limits['word_min']}-{limits['word_max']})"
        )

    for phrase in banned:
        issues.append(f'Contains a flagged template phrase: "{phrase}"')

    if exclamations > 1:
        issues.append(f"{exclamations} exclamation points — proposal-writer allows at most 1")

    return {
        "platform": platform,
        "word_count": word_count,
        "issues": issues,
        "passed": len(issues) == 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check a drafted proposal against platform norms and anti-patterns."
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="Path to a text file with the proposal. Omit to read from stdin.",
    )
    parser.add_argument(
        "--platform",
        "-p",
        choices=sorted(PLATFORM_LIMITS.keys()),
        default="generic",
        help="Which platform's norms to check against (default: generic).",
    )
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read().strip()
    else:
        text = sys.stdin.read().strip()

    if not text:
        sys.exit("Error: no proposal text given.")

    result = check(text, args.platform)

    print(f"Platform: {result['platform']}")
    print(f"Word count: {result['word_count']}")
    print()

    if result["passed"]:
        print("PASSED — no mechanical issues found.")
        print("(This checks length and banned phrases only — read it yourself too.)")
    else:
        print(f"FAILED — {len(result['issues'])} issue(s):")
        for issue in result["issues"]:
            print(f"  - {issue}")

    sys.exit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
