"""Newton's method as functional fixed-point iteration.

Ported from the Scala workshop (NewtonFunctional.sc).  The idea: a root
of f is a fixed point of the step x -> x - f(x)/f'(x).  We build a lazy
stream of successive estimates and stop when two in a row are close
enough.  Every function here is pure.
"""

from typing import Callable, Iterator


# start: iterate
def iterate(step: Callable[[float], float], x0: float) -> Iterator[float]:
    """Yield x0, step(x0), step(step(x0)), ... lazily and forever."""
    x = x0
    while True:
        yield x
        x = step(x)
# end: iterate


# start: converged
def converged_value(values: Iterator[float], eps: float) -> float:
    """Return the first value within eps of the one before it."""
    prev = next(values)
    for x in values:
        if abs(x - prev) < eps:
            return x
        prev = x
# end: converged


# start: newton
def newton(x0: float,
           f: Callable[[float], float],
           f_prime: Callable[[float], float],
           eps: float = 1e-10) -> float:
    """Find a root of f near x0 using Newton's method.

    Pure and higher-order: the same x0, f, and f_prime always give the
    same root, and f and f_prime are themselves passed in as functions.
    """
    step = lambda x: x - f(x) / f_prime(x)
    return converged_value(iterate(step, x0), eps)
# end: newton


if __name__ == '__main__':
    # 3x^2 + 5x - 7, with derivative 6x + 5
    def f(x):
        return 3 * x ** 2 + 5 * x - 7

    def f_prime(x):
        return 6 * x + 5

    root = newton(0.0, f, f_prime)
    print(f"root = {root:.6f}")
    print(f"f(root) = {f(root):.2e}")
