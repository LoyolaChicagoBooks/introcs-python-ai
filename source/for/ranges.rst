.. index:: range(), loop; range

.. _Ranges:

The ``range()`` Function
========================

Python's ``range()`` produces a sequence of integers on demand.  Paired with
``for``, it covers every counter-based loop pattern.

One-Argument Form: ``range(n)``
--------------------------------

.. index:: range(n)

.. code-block:: none

   range(n)   →  0, 1, 2, ..., n-1

Run it live and change ``n``:

.. try_examples::
   :height: 240px

   >>> for i in range(4):
   ...     print(i)
   ...
   0
   1
   2
   3

To see the full sequence at once, convert it to a list:

.. try_examples::
   :height: 200px

   >>> print(list(range(4)))
   [0, 1, 2, 3]

Two-Argument Form: ``range(start, stop)``
------------------------------------------

.. index:: range(start, stop)

.. code-block:: none

   range(start, stop)   →  start, start+1, ..., stop-1

Run it live:

.. try_examples::
   :height: 260px

   >>> for i in range(1, 6):
   ...     print(i)
   ...
   1
   2
   3
   4
   5

Note that ``stop`` is *exclusive* — the loop runs while ``i < stop``.

Three-Argument Form: ``range(start, stop, step)``
--------------------------------------------------

.. index:: range(start, stop, step)

.. code-block:: none

   range(start, stop, step)   →  start, start+step, start+2*step, ...

Counting by fives from 0 to 20.  Run it and change the step:

.. try_examples::
   :height: 200px

   >>> print(list(range(0, 25, 5)))
   [0, 5, 10, 15, 20]

The sequence stops *before* it would equal or exceed ``stop``.

The boundaries of ``range()`` are the classic source of off-by-one bugs.
Change ``start``, ``stop``, and ``step`` and watch which integers appear:

.. try_examples::
   :height: 300px

   >>> print(list(range(5)))           # 0 .. 4
   [0, 1, 2, 3, 4]
   >>> print(list(range(1, 6)))        # 1 .. 5  (stop is exclusive)
   [1, 2, 3, 4, 5]
   >>> print(list(range(0, 25, 5)))    # count by fives
   [0, 5, 10, 15, 20]
   >>> print(list(range(5, 0, -1)))    # count down
   [5, 4, 3, 2, 1]
   >>> for i in range(1, 6):
   ...     print(i, end=" ")
   ...
   1 2 3 4 5

Reverse Iteration
-----------------

.. index:: range; reverse, reversed()

A negative step counts downward.  Run it live:

.. try_examples::
   :height: 260px

   >>> for i in range(5, 0, -1):
   ...     print(i)
   ...
   5
   4
   3
   2
   1

``range(n-1, -1, -1)`` visits indices n-1 down to 0.

An alternative that reads more naturally is ``reversed(range(n))``:

.. try_examples::
   :height: 260px

   >>> for i in reversed(range(5)):
   ...     print(i)
   ...
   4
   3
   2
   1
   0

.. index:: range; lazy evaluation, range; memory efficiency

Range Objects Are Lazy
-----------------------

``range()`` does *not* build a list in memory — it computes each integer on
demand.  This makes ``range(1_000_000)`` just as cheap to create as
``range(5)``.  Only use ``list(range(...))`` when you actually need a list.

Summary
-------

.. list-table::
   :header-rows: 1
   :widths: 45 45

   * - Pattern
     - Python ``range()`` form
   * - Count from 0 to n-1
     - ``for i in range(n):``
   * - Count from a to b-1
     - ``for i in range(a, b):``
   * - Count from a to b-1 by k
     - ``for i in range(a, b, k):``
   * - Count down from n-1 to 0
     - ``for i in range(n-1, -1, -1):``
