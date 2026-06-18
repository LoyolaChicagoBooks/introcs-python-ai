.. index:: recursion, base case, recursive case, call stack
   ACM-IEEE CS2013; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2023; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2013; AL2 Algorithmic Strategies
   ACM-IEEE CS2023; AL2 Algorithmic Strategies

.. _Recursion-Intro:

Introduction to Recursion
=========================

A function is *recursive* if it calls itself.  This sounds circular, but
it works because every recursive call moves closer to a *base case* that
does not recurse.

The Structure of a Recursive Function
---------------------------------------

.. index:: recursion; structure

Every correct recursive function has:

1. **One or more base cases** — inputs small enough to answer directly
   without another recursive call.
2. **One or more recursive cases** — the function calls itself with a
   *simpler* or *smaller* argument, making progress toward a base case.

Factorial
---------

.. index:: factorial; recursive, factorial; iterative

The mathematical definition of factorial is itself recursive:

.. code-block:: none

   0! = 1                    (base case)
   n! = n × (n-1)!           (recursive case)

A recursive Python implementation follows that definition directly.  Run it
below and try a few small values of your own (keep ``n`` modest — each call
adds a stack frame):

.. try_examples::
   :height: 280px

   >>> def factorial_recursive(n: int) -> int:
   ...     if n < 0:
   ...         raise ValueError(f"factorial not defined for negative integers: {n}")
   ...     if n == 0:
   ...         return 1
   ...     return n * factorial_recursive(n - 1)
   ...
   >>> factorial_recursive(4)
   24
   >>> factorial_recursive(5)
   120

Trace for ``factorial_recursive(4)``:

.. code-block:: none

   factorial_recursive(4)
     = 4 * factorial_recursive(3)
     = 4 * 3 * factorial_recursive(2)
     = 4 * 3 * 2 * factorial_recursive(1)
     = 4 * 3 * 2 * 1 * factorial_recursive(0)
     = 4 * 3 * 2 * 1 * 1
     = 24

Both versions reject negative inputs with a ``ValueError``, because
factorial is undefined for negative integers.  Raising an exception here
is the right choice: a negative argument is a programming error, not an
expected outcome.

Factorial is *not* an ideal candidate for recursion in Python.  It
requires one stack frame per integer, so ``factorial_recursive(1000)``
will hit the default recursion limit.  The iterative version is simpler,
faster, and scales to any size.  The loop multiplies ``result`` by every
integer from 2 up to ``n``, accumulating the product one factor at a time.
Calling it with large values works without any risk of hitting the recursion
limit — run it and try ``factorial_iterative(1000)``:

.. try_examples::
   :height: 320px

   >>> def factorial_iterative(n: int) -> int:
   ...     if n < 0:
   ...         raise ValueError(f"factorial not defined for negative integers: {n}")
   ...     result = 1
   ...     for i in range(2, n + 1):
   ...         result *= i
   ...     return result
   ...
   >>> factorial_iterative(5)
   120
   >>> factorial_iterative(100)
   93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

Python's standard library also provides ``math.factorial(n)``, which is
implemented in C and is the best choice in real code.

.. index:: stack frame; recursion, call stack; depth

The Call Stack
--------------

.. index:: call stack; recursion

Each call to a recursive function creates a new *stack frame* holding its
own local variables and the return address.  When the base case returns,
frames unwind in reverse order.  For ``factorial_recursive(4)``, four
frames are pushed before any frame is popped.

Fibonacci Numbers
-----------------

.. index:: Fibonacci; recursive, Fibonacci; iterative

The base cases return 0 and 1 directly.  Every other call splits into two
smaller sub-problems, mirroring the mathematical definition F(n) = F(n−1) + F(n−2).
Run it below to verify it produces the expected sequence for the first eight
values, then increase the loop range.  Try ``fib_recursive(35)`` and notice the
pause — the exponential blow-up is real.  (Keep ``n`` well under 1000 to avoid
the recursion limit.)

.. try_examples::
   :height: 320px

   >>> def fib_recursive(n: int) -> int:
   ...     if n < 0:
   ...         raise ValueError(f"Fibonacci not defined for negative indices: {n}")
   ...     if n <= 1:
   ...         return n
   ...     return fib_recursive(n - 1) + fib_recursive(n - 2)
   ...
   >>> for i in range(8):
   ...     print(fib_recursive(i), end=" ")
   ...
   0 1 1 2 3 5 8 13

Both versions reject negative ``n`` for the same reason: the Fibonacci
sequence is conventionally defined only for non-negative indices, and a
negative argument almost certainly indicates a caller bug.

This is correct but extremely slow: ``fib_recursive(n)`` makes two
recursive calls, so the total number of calls grows exponentially —
``fib_recursive(40)`` makes over a billion calls.  Like factorial,
Fibonacci is *not* an ideal candidate for recursion.

The iterative version computes the same result in O(N) time with no
stack growth at all.  The loop keeps only the two most recent values, advancing
the pair forward on each iteration.  This requires O(1) space and O(N) time,
with no stack growth.  Values that would be impossibly slow for the naive
recursive version are computed instantly — run it and try ``fib_iterative(500)``:

.. try_examples::
   :height: 340px

   >>> def fib_iterative(n: int) -> int:
   ...     if n < 0:
   ...         raise ValueError(f"Fibonacci not defined for negative indices: {n}")
   ...     if n <= 1:
   ...         return n
   ...     prev, curr = 0, 1
   ...     for _ in range(2, n + 1):
   ...         prev, curr = curr, prev + curr
   ...     return curr
   ...
   >>> fib_iterative(40)
   102334155
   >>> fib_iterative(100)
   354224848179261915075

Use the iterative form (or memoisation — see :ref:`Recursion-Examples`)
whenever you need Fibonacci for large ``n``.

Python's Recursion Limit
-------------------------

.. index:: sys.setrecursionlimit, recursion limit, RecursionError

Python limits recursive calls to prevent the call stack from growing
without bound.  The default limit is 1 000.  You can inspect or raise it:

.. code-block:: python

   import sys
   print(sys.getrecursionlimit())   # 1000

   sys.setrecursionlimit(5000)      # use with caution

Hitting the limit raises ``RecursionError``.

.. index::
   tail recursion
   single: van Rossum, Guido; TCO decision

No Tail-Call Optimisation
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: tail-call optimisation, TCO

Some languages (Scheme, Haskell, Kotlin) detect *tail calls* — recursive
calls that are the very last action of a function — and reuse the current
stack frame instead of creating a new one.  **Python does not perform
tail-call optimisation.**  Even a perfectly tail-recursive function
allocates a new frame on every call, so it hits the recursion limit just
as fast as any other recursive function.  This is a deliberate design
decision: Guido van Rossum wanted stack traces to always show the full
call history, which TCO would erase.

Security Implications of Unbounded Recursion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: recursion; security, denial of service; recursion, stack exhaustion

When a recursive function is called with input that controls the depth —
for example, parsing a deeply-nested data structure received from a
network — an attacker can craft input that exhausts the call stack.
Stack exhaustion crashes the Python interpreter or, in a server context,
terminates the worker process.  This is a form of **denial-of-service
(DoS)**.

Mitigations:

- **Validate depth before recursing.** Reject or truncate input whose
  nesting depth exceeds a safe threshold.
- **Use an explicit stack.** Rewrite the algorithm iteratively with a
  list acting as a stack; then the "stack" lives on the heap and is
  bounded only by available memory, not the call-stack limit.
- **Do not raise ``sys.setrecursionlimit`` in production** in response
  to untrusted input — that only delays the crash and may exhaust
  memory entirely.

.. index:: recursion; when to use, divide and conquer, tree traversal

When to Use Recursion
---------------------

Recursion is natural when the problem has an inherently recursive
structure: tree traversal, divide-and-conquer algorithms (merge sort,
quicksort, binary search), and problems defined recursively (GCD,
directory trees, fractals).

Simple counting problems like factorial and Fibonacci belong in an
iterative loop.  A good rule of thumb: if you can easily describe
the algorithm with a ``for`` loop, prefer the loop.
