"""Closures, partial application, and function composition."""

from functools import partial


# start: make_multiplier
def make_multiplier(factor: int):
    """Return a function that multiplies its argument by factor.

    The returned function "closes over" factor — it remembers the value
    even after make_multiplier has returned.
    """
    def multiply(x: int) -> int:
        return x * factor
    return multiply
# end: make_multiplier


# start: make_counter
def make_counter():
    """Return a function that returns 1, 2, 3, ... on each call.

    The count lives in the enclosing scope; ``nonlocal`` lets the inner
    function update it.  This is a closure that owns mutable state — handy,
    but no longer a pure function.
    """
    count = 0

    def next_value() -> int:
        nonlocal count
        count += 1
        return count
    return next_value
# end: make_counter


# start: partial
def power(base: float, exponent: float) -> float:
    """Raise base to exponent."""
    return base ** exponent
# end: partial


if __name__ == '__main__':
    triple = make_multiplier(3)
    print(triple(10))

    counter = make_counter()
    print(counter(), counter(), counter())

    square = partial(power, exponent=2)
    print(square(9))
