"""Higher-order functions: map, filter, reduce, scan, and composition."""

from functools import reduce
from itertools import accumulate


# start: map_filter
def celsius_to_fahrenheit(c: float) -> float:
    """Convert a Celsius temperature to Fahrenheit (a pure function)."""
    return c * 9 / 5 + 32


def is_freezing(c: float) -> bool:
    """True if the Celsius temperature is at or below freezing."""
    return c <= 0
# end: map_filter


# start: reduce
def product(numbers: list) -> int:
    """Multiply every number together, starting from 1."""
    return reduce(lambda total, n: total * n, numbers, 1)
# end: reduce


# start: scan
def running_total(amounts: list) -> list:
    """Return the balance after each amount, starting from 0.

    Like Scala's scanLeft, this keeps every intermediate sum, not just the
    final one that reduce would give.
    """
    return list(accumulate(amounts, initial=0))
# end: scan


# start: compose
def compose(*funcs):
    """Return a function that applies funcs right to left.

    compose(f, g)(x) == f(g(x)).  With no arguments it returns the
    identity function, so composition has a sensible starting point.
    """
    return reduce(lambda f, g: lambda x: f(g(x)), funcs, lambda x: x)
# end: compose


if __name__ == '__main__':
    temps = [-5, 0, 12, 100]
    print(list(map(celsius_to_fahrenheit, temps)))
    print(list(filter(is_freezing, temps)))
    print(product([1, 2, 3, 4, 5]))
    print(running_total([10, -4, 3, -8]))

    # double-then-increment, read right to left
    transform = compose(lambda x: x + 1, lambda x: x * 2)
    print(transform(10))
