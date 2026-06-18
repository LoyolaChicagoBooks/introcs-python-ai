.. index:: Newton's method, Monte Carlo method, generator; stream
   functional programming; numerical, fixed point
   ACM-IEEE CS2013; PL2 Functional Programming
   ACM-IEEE CS2023; PL2 Functional Programming

.. _Functional-Numerical:

Worked Examples: Newton and Monte Carlo
=======================================

.. note::

   *Source:* Ported from the numerical-explorations examples in Läufer and
   Thiruvathukal, *Type-Safe Functional Programming for Computer Science and
   Data Science* (IEEE eScience 2025 workshop;
   `scalaworkshop.cs.luc.edu <https://scalaworkshop.cs.luc.edu>`_), recast
   from Scala into Python.

Two classic numerical problems show the functional style at work on real
computation.  Both lean on the generators you met in the
:ref:`Recursion <Recursion-Examples>` chapter: a generator is a lazy,
potentially endless *stream* of values, and functional code loves to build
a stream and then describe what to do with it.

Newton's Method as Iteration
----------------------------

Newton's method finds a root of an equation *f(x) = 0* by improving a guess
over and over: from a guess ``x`` it computes a better one,
``x - f(x)/f'(x)``, and repeats until two successive guesses are close
enough.  Phrased functionally, a root is a **fixed point** of the step
function — a value the step no longer changes.

We can split that into three small pieces, each pure.  ``iterate`` produces
the endless stream of guesses; ``converged_value`` walks a stream until two
neighbours are within ``eps``; and ``newton`` ties them together, taking the
function ``f`` and its derivative ``f_prime`` as arguments:

.. literalinclude:: ../../examples/introcs-python/functional/newton.py
   :language: python
   :start-after: # start: iterate
   :end-before: # end: iterate

.. literalinclude:: ../../examples/introcs-python/functional/newton.py
   :language: python
   :start-after: # start: converged
   :end-before: # end: converged

.. literalinclude:: ../../examples/introcs-python/functional/newton.py
   :language: python
   :start-after: # start: newton
   :end-before: # end: newton

``newton`` is higher-order twice over: it *takes* two functions and it
*builds* a third (``step``, a closure over ``f`` and ``f_prime``).  The loop
and the stopping rule live in ``converged_value``, reusable for any
iterative method, not just this one.  Try it on *3x² + 5x − 7*, whose
derivative is *6x + 5*:

.. try_examples::
   :height: 420px

   >>> def iterate(step, x0):
   ...     x = x0
   ...     while True:
   ...         yield x
   ...         x = step(x)
   ...
   >>> def converged_value(values, eps):
   ...     prev = next(values)
   ...     for x in values:
   ...         if abs(x - prev) < eps:
   ...             return x
   ...         prev = x
   ...
   >>> def newton(x0, f, f_prime, eps=1e-10):
   ...     step = lambda x: x - f(x) / f_prime(x)
   ...     return converged_value(iterate(step, x0), eps)
   ...
   >>> root = newton(0.0, lambda x: 3 * x ** 2 + 5 * x - 7, lambda x: 6 * x + 5)
   >>> round(root, 6)
   0.906718
   >>> abs(3 * root ** 2 + 5 * root - 7) < 1e-9
   True

Monte Carlo π: Imperative vs. Functional
----------------------------------------

The Monte Carlo method estimates π by throwing random darts at the unit
square and counting how many land inside the quarter circle: the fraction
inside approaches π/4.  (The :ref:`Case Studies <Case-Study-Monte-Carlo>`
chapter develops the same idea as a full data pipeline.)

The imperative version is a loop with a mutable counter — a faithful picture
of what the machine does:

.. literalinclude:: ../../examples/introcs-python/functional/monte_carlo.py
   :language: python
   :start-after: # start: imperative
   :end-before: # end: imperative

The functional version says *what* is being computed instead of *how* to
step through it.  A pure predicate ``in_circle`` decides whether a dart
counts; ``darts`` is an endless stream of random points; and the estimate is
just "take ``num_darts`` of them and count the ones in the circle":

.. literalinclude:: ../../examples/introcs-python/functional/monte_carlo.py
   :language: python
   :start-after: # start: functional
   :end-before: # end: functional

Read the functional version aloud and it almost states the method: take
this many darts, keep the ones inside the circle, scale by four.  There is
no index variable and no counter to get wrong.  Seeding the generator makes
the result reproducible:

.. try_examples::
   :height: 360px

   >>> import random
   >>> from itertools import islice
   >>> def in_circle(point):
   ...     x, y = point
   ...     return x * x + y * y <= 1.0
   ...
   >>> def darts(rng):
   ...     while True:
   ...         yield (rng.random(), rng.random())
   ...
   >>> def estimate_pi(num_darts, rng):
   ...     hits = sum(1 for p in islice(darts(rng), num_darts) if in_circle(p))
   ...     return 4.0 * hits / num_darts
   ...
   >>> estimate_pi(100_000, random.Random(0))
   3.14844

Both versions compute the same estimate — given the same stream of random
darts they return the same number.  The functional one simply describes the
computation at a higher level, and its pieces (``in_circle``, the stream,
the count) are each independently testable, which is where we turn next.
