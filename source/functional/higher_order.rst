.. index:: higher-order function, map(), filter(), functools.reduce
   predicate, fold, itertools.accumulate, scanLeft, running total
   ACM-IEEE CS2013; PL2 Functional Programming
   ACM-IEEE CS2023; PL2 Functional Programming

.. _Higher-Order-Functions:

Higher-Order Functions
======================

A **higher-order function** is a function that takes another function as an
argument or returns one as its result.  You met the idea in
:ref:`Functions as Values <Functions-as-Values>`: ``sorted`` is
higher-order because it accepts a ``key`` function.  Three higher-order
functions come up so often that Python builds them in — ``map``,
``filter``, and ``reduce``.  Each takes a function and a sequence and gives
back a result, with no loop and no mutable counter in sight.

map: Transform Every Element
----------------------------

``map(f, seq)`` applies ``f`` to every element of ``seq``.  It returns a
lazy iterator, so wrap it in ``list`` to see the results:

.. try_examples::
   :height: 280px

   >>> def fahrenheit(c):
   ...     return c * 9 / 5 + 32
   ...
   >>> temps = [-5, 0, 12, 100]
   >>> list(map(fahrenheit, temps))
   [23.0, 32.0, 53.6, 212.0]

This is the same transformation a list comprehension expresses, and for
most code a comprehension reads more clearly:

.. try_examples::
   :height: 260px

   >>> nums = [1, 2, 3, 4, 5]
   >>> list(map(lambda n: n * n, nums))
   [1, 4, 9, 16, 25]
   >>> [n * n for n in nums]
   [1, 4, 9, 16, 25]

The guidance from :ref:`List Comprehensions <List-Comprehensions>` still
holds: prefer the comprehension when you would otherwise write a small
``lambda``, and reach for ``map`` when you already have a named function to
apply (``map(fahrenheit, temps)`` reads better than repeating its body).

filter: Keep the Elements That Qualify
--------------------------------------

``filter(predicate, seq)`` keeps only the elements for which ``predicate``
returns a true value.  A **predicate** is just a function that returns a
boolean:

.. try_examples::
   :height: 280px

   >>> def is_freezing(c):
   ...     return c <= 0
   ...
   >>> temps = [-5, 0, 12, 100]
   >>> list(filter(is_freezing, temps))
   [-5, 0]

Again there is a comprehension form, ``[c for c in temps if c <= 0]``, and
again it is usually the clearer of the two.  The value of knowing ``map``
and ``filter`` is partly that you will meet them in other people's code and
in other languages, and partly that they name the two most common shapes of
data processing: *transform each element*, and *keep some elements*.

reduce: Combine Everything Into One Value
-----------------------------------------

The third shape is *combine the elements into a single value* — a sum, a
product, a maximum.  ``functools.reduce(f, seq, start)`` folds the sequence
up by repeatedly applying ``f`` to the running result and the next element:

.. try_examples::
   :height: 300px

   >>> from functools import reduce
   >>> reduce(lambda total, n: total * n, [1, 2, 3, 4, 5], 1)
   120
   >>> reduce(lambda total, n: total + n, [1, 2, 3, 4, 5], 0)
   15

The ``start`` value (``1`` for a product, ``0`` for a sum) is what
``reduce`` returns for an empty sequence, which is why it is also called the
*identity* for the operation.  Most common reductions already have a
dedicated built-in — ``sum``, ``max``, ``min``, ``all``, ``any`` — and you
should prefer those when they exist.  ``reduce`` is for the cases that do
not, such as a running product:

.. literalinclude:: ../../examples/introcs-python/functional/higher_order.py
   :language: python
   :start-after: # start: reduce
   :end-before: # end: reduce

A wrapper like ``product`` is worth writing because the name says what the
fold *means*, where the bare ``reduce(lambda ...)`` makes the reader work it
out.  That is the recurring lesson of higher-order functions: they let you
package a *pattern of computation* behind a meaningful name.

accumulate: Keep the Running Results
------------------------------------

``reduce`` throws away its work in progress and returns only the final
value.  Often you want the *whole trail* of intermediate results instead — a
running total, a running maximum, a bank balance after each transaction.
Scala calls this ``scanLeft`` because it scans from the left, accumulating as
it goes; Python provides it as ``itertools.accumulate``.

Where ``reduce`` returns one number, ``accumulate`` yields the accumulator
after each step:

.. try_examples::
   :height: 300px

   >>> from itertools import accumulate
   >>> list(accumulate([1, 2, 3, 4, 5]))             # running sums
   [1, 3, 6, 10, 15]
   >>> from functools import reduce
   >>> reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])   # reduce keeps only the last
   15

By default ``accumulate`` adds, but you can pass any function of two
arguments to combine differently, and an ``initial`` value to seed the
running result — which is exactly Scala's ``scanLeft(initial)(op)``:

.. try_examples::
   :height: 320px

   >>> import operator
   >>> from itertools import accumulate
   >>> list(accumulate([1, 2, 3, 4, 5], operator.mul))   # running products
   [1, 2, 6, 24, 120]
   >>> list(accumulate([10, -4, 3, -8], initial=0))      # balance after each change
   [0, 10, 6, 9, 1]

The last example reads as a tiny bank statement: start at ``0``, then show
the balance after a deposit of ``10``, a withdrawal of ``4``, and so on.
Naming the pattern keeps the intent clear:

.. literalinclude:: ../../examples/introcs-python/functional/higher_order.py
   :language: python
   :start-after: # start: scan
   :end-before: # end: scan

So ``reduce`` answers "what is the final total?" and ``accumulate`` answers
"what was the total at every point along the way?"  Reach for the scan
whenever the history of the computation is as interesting as its result.
