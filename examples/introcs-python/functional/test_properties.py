"""Property-based tests for the chapter's pure functions.

Instead of hand-picking a few inputs, we state a property that must hold
for *every* input and let hypothesis search for a counterexample.  Run
with:  python -m pytest test_properties.py
"""

import math

from hypothesis import given, strategies as st

from pure_core import average, parse_scores
from newton import newton


# start: invariant
@given(st.lists(st.integers(min_value=-10 ** 6, max_value=10 ** 6), min_size=1))
def test_average_within_bounds(scores):
    """The mean of a non-empty list lies between its smallest and largest."""
    assert min(scores) <= average(scores) <= max(scores)
# end: invariant


# start: roundtrip
@given(st.lists(st.integers()))
def test_reverse_roundtrip(xs):
    """Reversing a list twice gives back the original."""
    assert list(reversed(list(reversed(xs)))) == xs
# end: roundtrip


# start: oracle
@given(st.floats(min_value=1.0, max_value=1e6))
def test_newton_matches_sqrt(c):
    """Newton's method on x^2 - c finds the square root math.sqrt gives."""
    root = newton(c, lambda x: x * x - c, lambda x: 2 * x)
    assert math.isclose(root, math.sqrt(c), rel_tol=1e-6)
# end: oracle
