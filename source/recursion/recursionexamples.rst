.. index:: recursion; examples, GCD; recursive, binary search; recursive,
           generator; factorial, generator; Fibonacci
   ACM-IEEE CS2013; PL2 Functional Programming
   ACM-IEEE CS2023; PL2 Functional Programming
   ACM-IEEE CS2013; AL1 Basic Analysis
   ACM-IEEE CS2023; AL1 Basic Analysis
   ACM-IEEE CS2013; AL2 Algorithmic Strategies
   ACM-IEEE CS2023; AL2 Algorithmic Strategies
   ACM-IEEE CS2013; OS8 File Systems
   ACM-IEEE CS2023; OS8 File Systems

.. _Recursion-Examples:

Recursion Examples
==================

GCD — Euclidean Algorithm
--------------------------

.. index:: GCD; recursive, Euclidean algorithm

The greatest common divisor of two integers has an elegant recursive
definition:

.. code-block:: none

   gcd(a, 0) = a                  (base case)
   gcd(a, b) = gcd(b, a % b)     (recursive case)

Run it below and try a few pairs of your own:

.. try_examples::
   :height: 240px

   >>> def gcd(a: int, b: int) -> int:
   ...     if b == 0:
   ...         return a
   ...     return gcd(b, a % b)
   ...
   >>> gcd(48, 18)
   6
   >>> gcd(100, 75)
   25

Each call reduces ``b`` toward 0 because ``a % b < b`` for any ``b > 0``.
Python's standard library provides ``math.gcd`` which uses the same
algorithm.

Recursive Binary Search
------------------------

.. index:: binary search; recursive

Binary search on a sorted list can be expressed recursively: check the
midpoint, then recurse on the left or right half:

.. literalinclude:: ../../examples/introcs-python/recursion/binary_search.py
   :language: python
   :start-after: # start: binary_search
   :end-before: # end: binary_search

.. code-block:: python

   data = [-5, 2, 8, 9, 12, 22]
   print(binary_search(data, 9))    # 3
   print(binary_search(data, 7))    # -1

Each recursive call halves the search space, giving O(log N) depth.

Inner Helper Pattern
^^^^^^^^^^^^^^^^^^^^^

.. index:: recursion; inner helper, nested function; recursive helper

The version above exposes ``lo`` and ``hi`` as optional parameters, so
the recursive signature doubles as the public API.  An alternative hides
the bounds inside a nested function, giving callers a clean
two-argument interface:

.. literalinclude:: ../../examples/introcs-python/recursion/binary_search_helper.py
   :language: python
   :start-after: # start: binary_search_helper
   :end-before: # end: binary_search_helper

The outer ``binary_search`` owns the list and kicks off the search with
the full range.  The inner ``helper`` is the recursive engine — callers
never see ``low`` or ``high`` and cannot accidentally pass wrong values
for them.

.. code-block:: python

   data = [-5, 2, 8, 9, 12, 22]
   print(binary_search(data, 9))   # 3
   print(binary_search(data, 7))   # -1

Property-Based Testing with Hypothesis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: Hypothesis; property-based testing, property-based testing, pytest; Hypothesis

Testing by hand covers only the cases you think of.  *Property-based
testing* generates hundreds of random inputs automatically and checks
that a stated property holds for all of them.  The ``hypothesis``
library does this in Python:

.. literalinclude:: ../../examples/introcs-python/recursion/binary_search_helper.py
   :language: python
   :start-after: # start: hypothesis_test
   :end-before: # end: hypothesis_test

``@given(st.lists(st.integers()), st.integers())`` tells Hypothesis to
generate a random sorted list and a random key on every run — hundreds
of variations, including empty lists, single-element lists, and keys
outside the array's range.  The two properties asserted are:

- if ``key`` is absent, the result must be ``-1``
- if ``key`` is present, the returned index must point to it

Install Hypothesis with ``pip install hypothesis``, then run the test
with ``pytest binary_search_helper.py``.

Flattening a Nested List
------------------------

.. index:: flatten; recursive, nested list

Some problems only make sense recursively.  Flattening an arbitrarily
nested list has no clean iterative equivalent.  For each element, the function
checks whether it is itself a list.  If it is, it recurses into it; if not, it
appends the value directly.  Any depth of nesting is handled naturally because
the recursion keeps going until it reaches a non-list item.  Run it and try a
more deeply nested list of your own:

.. try_examples::
   :height: 300px

   >>> def flatten(lst: list) -> list:
   ...     result = []
   ...     for item in lst:
   ...         if isinstance(item, list):
   ...             result.extend(flatten(item))
   ...         else:
   ...             result.append(item)
   ...     return result
   ...
   >>> nested = [1, [2, 3], [4, [5, 6]], 7]
   >>> flatten(nested)
   [1, 2, 3, 4, 5, 6, 7]

.. index:: pathlib; recursive traversal, file system; tree traversal

Directory Tree Traversal
------------------------

.. index:: os.walk; recursive, directory traversal

File systems are trees — a natural fit for recursion:

.. code-block:: python

   from pathlib import Path

   def print_tree(path, indent: int = 0) -> None:
       print("  " * indent + path.name)
       if path.is_dir():
           for child in sorted(path.iterdir()):
               print_tree(child, indent + 1)

Each call prints the current entry's name, indented by its depth, then
recurses into each child if the entry is a directory.  Files are leaf nodes —
they print their name and return immediately.  Calling it on the current
directory walks the entire tree:

.. code-block:: python

   print_tree(Path("."))

The function calls itself for each subdirectory, unwinding naturally
when a directory has no more children.

Memoisation with ``lru_cache``
--------------------------------

.. index:: functools.lru_cache, memoisation

The naive recursive Fibonacci is exponential because it recomputes the
same values repeatedly.  ``functools.lru_cache`` stores results
automatically.  The ``@lru_cache`` decorator wraps ``fib`` so that the first
time any value is computed it is stored; subsequent calls with the same argument
return the cached result instantly.  The recursive structure of the code is
unchanged — only its performance profile improves.  Run it and try ``fib(200)``,
which would be hopeless without the cache:

.. try_examples::
   :height: 280px

   >>> from functools import lru_cache
   >>> @lru_cache(maxsize=None)
   ... def fib(n: int) -> int:
   ...     if n <= 1:
   ...         return n
   ...     return fib(n - 1) + fib(n - 2)
   ...
   >>> fib(50)
   12586269025

With caching, each value of ``fib(n)`` is computed exactly once,
reducing the total work to O(N).

Generators for Sequences with a Ceiling
-----------------------------------------

.. index:: generator; infinite sequence, yield, itertools.takewhile

For sequences defined by a recurrence — like factorials and Fibonacci
numbers — Python *generators* offer a third style that is neither
recursive nor a plain loop.  A generator function uses ``yield`` to
produce one value at a time, suspending execution between calls.  This
makes it natural to express "generate values indefinitely, and let the
caller decide when to stop."

Infinite Factorial Generator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: generator; factorial

.. literalinclude:: ../../examples/introcs-python/recursion/generators.py
   :language: python
   :start-after: # start: factorials
   :end-before: # end: factorials

The generator runs forever by design.  To collect only the values up to
a ceiling, use ``itertools.takewhile``:

.. code-block:: python

   from itertools import takewhile

   for f in takewhile(lambda x: x <= 1_000_000, factorials()):
       print(f)

Output:

.. code-block:: none

   1
   1
   2
   6
   24
   120
   720
   5040
   40320
   362880

You can also write a self-contained generator that accepts the ceiling
directly — useful when you want a single, reusable function:

.. literalinclude:: ../../examples/introcs-python/recursion/generators.py
   :language: python
   :start-after: # start: factorials_up_to
   :end-before: # end: factorials_up_to

.. code-block:: python

   print(list(factorials_up_to(1_000_000)))

Output:

.. code-block:: none

   [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

Infinite Fibonacci Generator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: generator; Fibonacci

.. literalinclude:: ../../examples/introcs-python/recursion/generators.py
   :language: python
   :start-after: # start: fibonacci
   :end-before: # end: fibonacci

.. code-block:: python

   from itertools import takewhile

   fibs = list(takewhile(lambda x: x <= 1000, fibonacci()))
   print(fibs)

Output:

.. code-block:: none

   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

Again, a ceiling-aware version keeps the intent local to the function:

.. literalinclude:: ../../examples/introcs-python/recursion/generators.py
   :language: python
   :start-after: # start: fibonacci_up_to
   :end-before: # end: fibonacci_up_to

.. code-block:: python

   print(list(fibonacci_up_to(1000)))

Output:

.. code-block:: none

   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

.. index:: generator; advantages, lazy evaluation; generators

Why Generators?
^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Property
     - Generators
   * - Memory
     - O(1) — only the current value is in memory at any time
   * - Stack depth
     - O(1) — no recursive frames; no ``RecursionError``
   * - Early termination
     - Natural with ``takewhile``, ``break``, or ``next()``
   * - Composability
     - Pipe generators through ``itertools`` functions freely

Generators are the idiomatic Python choice for producing a potentially
large (or infinite) sequence of values one at a time.  They combine the
clarity of recursive definitions with the efficiency of iterative loops.
