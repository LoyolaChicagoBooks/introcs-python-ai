"""Functional core, imperative shell.

All the logic lives in small pure functions that are easy to test.  The
only side effects — reading a file, printing — live in a thin shell that
does no computing of its own.
"""

from pathlib import Path


# start: pure_core
def parse_scores(text: str) -> list:
    """Turn raw text into a list of floats, one per non-empty line."""
    return [float(line) for line in text.splitlines() if line.strip()]


def average(scores: list) -> float:
    """The mean of a list of numbers (0.0 for an empty list)."""
    return sum(scores) / len(scores) if scores else 0.0


def letter_grade(avg: float) -> str:
    """Map a numeric average to a letter grade."""
    for cutoff, letter in [(90, "A"), (80, "B"), (70, "C"), (60, "D")]:
        if avg >= cutoff:
            return letter
    return "F"
# end: pure_core


# start: shell
def report(path: str) -> None:
    """Imperative shell: do the I/O, delegate every decision to pure functions."""
    text = Path(path).read_text()          # effect: read the world
    scores = parse_scores(text)
    avg = average(scores)
    print(f"average {avg:.1f} -> {letter_grade(avg)}")   # effect: change the world
# end: shell


if __name__ == '__main__':
    sample = "92\n85\n79\n"
    scores = parse_scores(sample)
    print(scores)
    print(f"{average(scores):.1f}")
    print(letter_grade(average(scores)))
