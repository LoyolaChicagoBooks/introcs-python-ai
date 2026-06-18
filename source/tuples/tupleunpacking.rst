.. index:: tuple unpacking, multiple assignment, swap variables

.. _Tuple-Unpacking:

Tuple Unpacking
===============

*Tuple unpacking* (also called *destructuring*) assigns each element of
a tuple to a separate variable in one statement.

Basic Unpacking
---------------

.. index:: tuple unpacking; basic

Try it live and unpack a tuple of your own:

.. try_examples::
   :height: 220px

   >>> point = (3, 7)
   >>> x, y = point
   >>> print(x, y)
   3 7

The number of variables on the left must match the number of elements
in the tuple (or you get a ``ValueError``).

Swapping Variables
------------------

.. index:: swap; variables

The cleanest way to swap two variables in Python uses tuple unpacking.
Try it live:

.. try_examples::
   :height: 220px

   >>> a, b = 10, 20
   >>> a, b = b, a
   >>> print(a, b)
   20 10

Python evaluates the right-hand side completely before assigning, so no
temporary variable is needed.

Unpacking Function Return Values
----------------------------------

.. index:: tuple; multiple return values

A function can return multiple values as a tuple, and the caller can
unpack them.  Try it live and pass a different list:

.. try_examples::
   :height: 260px

   >>> def min_max(nums: list) -> tuple:
   ...     return min(nums), max(nums)
   ...
   >>> lo, hi = min_max([3, 1, 4, 1, 5, 9])
   >>> print(lo, hi)
   1 9

Unpacking in ``for`` Loops with ``zip()``
------------------------------------------

.. index:: zip(), for; tuple unpacking

``zip(a, b)`` pairs up elements from two sequences.  Unpacking in the
``for`` heading processes both at once.  Try it live and edit the lists:

.. try_examples::
   :height: 280px

   >>> names = ["Alice", "Bob", "Carol"]
   >>> scores = [88, 73, 95]
   >>> for name, score in zip(names, scores):
   ...     print(f"{name}: {score}")
   ...
   Alice: 88
   Bob: 73
   Carol: 95

``zip()`` stops at the shortest sequence.  Use ``zip(strict=True)`` in
Python 3.10+ to raise an error if the sequences have different lengths.

.. index:: star expression; unpacking, extended unpacking

Extended Unpacking
------------------

.. index:: tuple unpacking; *rest

A ``*`` prefix captures the "rest" of the sequence into a list.  Try it
live and move the ``*`` to a different position:

.. try_examples::
   :height: 300px

   >>> first, *rest = [1, 2, 3, 4, 5]
   >>> print(first)   # 1
   1
   >>> print(rest)    # [2, 3, 4, 5]
   [2, 3, 4, 5]
   >>> *body, last = [1, 2, 3, 4, 5]
   >>> print(body)    # [1, 2, 3, 4]
   [1, 2, 3, 4]
   >>> print(last)    # 5
   5

Experiment with unpacking below — try changing the number of variables
on the left and watch when Python raises a ``ValueError``:

.. try_examples::
   :height: 300px

   >>> a, b = 10, 20
   >>> a, b = b, a          # swap, no temporary needed
   >>> print("swapped:", a, b)
   swapped: 20 10
   >>> names = ["Alice", "Bob", "Carol"]
   >>> scores = [88, 73, 95]
   >>> for name, score in zip(names, scores):
   ...     print(f"{name}: {score}")
   ...
   Alice: 88
   Bob: 73
   Carol: 95
   >>> first, *rest = [1, 2, 3, 4, 5]
   >>> print("first:", first, " rest:", rest)
   first: 1  rest: [2, 3, 4, 5]
