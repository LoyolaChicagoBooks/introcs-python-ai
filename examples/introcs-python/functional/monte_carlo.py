"""Monte Carlo estimate of pi, imperative vs. functional.

Ported from the Scala workshop (MonteCarloPi*.sc).  Throw random darts
at the unit square; the fraction landing inside the quarter circle
approaches pi/4.  The two versions compute the same thing in two styles.
"""

import random
from itertools import islice
from typing import Iterator, Tuple


# start: imperative
def estimate_pi_imperative(num_darts: int, rng: random.Random) -> float:
    """Estimate pi with an explicit loop and a mutable counter."""
    in_circle = 0
    for _ in range(num_darts):
        x, y = rng.random(), rng.random()
        if x * x + y * y <= 1.0:
            in_circle += 1
    return 4.0 * in_circle / num_darts
# end: imperative


# start: functional
def in_circle(point: Tuple[float, float]) -> bool:
    """True if the point lies inside the unit circle (a pure predicate)."""
    x, y = point
    return x * x + y * y <= 1.0


def darts(rng: random.Random) -> Iterator[Tuple[float, float]]:
    """An endless lazy stream of random darts in the unit square."""
    while True:
        yield (rng.random(), rng.random())


def estimate_pi_functional(num_darts: int, rng: random.Random) -> float:
    """Estimate pi by counting the darts that satisfy in_circle."""
    hits = sum(1 for point in islice(darts(rng), num_darts) if in_circle(point))
    return 4.0 * hits / num_darts
# end: functional


if __name__ == '__main__':
    print(estimate_pi_imperative(1_000_000, random.Random(0)))
    print(estimate_pi_functional(1_000_000, random.Random(0)))
