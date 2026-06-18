.. index:: list comprehension
   ACM-IEEE CS2013; PL2 Functional Programming
   ACM-IEEE CS2023; PL2 Functional Programming

.. _List-Comprehensions:

List Comprehensions
===================


A common pattern with ``for`` loops is building a new list by transforming
or filtering an existing sequence.  Run it live:

.. try_examples::
   :height: 240px

   >>> squares = []
   >>> for n in range(1, 6):
   ...     squares.append(n ** 2)
   ...
   >>> print(squares)
   [1, 4, 9, 16, 25]

Python provides a compact notation for exactly this pattern called a
*list comprehension*:

.. code-block:: none

   [expression  for  item  in  iterable]

The result is a new list containing ``expression`` evaluated once for each
``item`` in ``iterable``.

Basic Form
----------

.. index:: list comprehension; basic form

The squares example above becomes a single line.  Run it live:

.. try_examples::
   :height: 220px

   >>> squares = [n ** 2 for n in range(1, 6)]
   >>> print(squares)
   [1, 4, 9, 16, 25]

More examples:

.. try_examples::
   :height: 220px

   >>> # ASCII codes of each character in a string
   >>> codes = [ord(ch) for ch in "hello"]
   >>> print(codes)
   [104, 101, 108, 108, 111]

.. try_examples::
   :height: 240px

   >>> # Lengths of each word in a list
   >>> words = ["cat", "elephant", "ox"]
   >>> lengths = [len(w) for w in words]
   >>> print(lengths)
   [3, 8, 2]

Filtered Form
-------------

.. index:: list comprehension; with condition

Add an ``if`` clause to keep only items that satisfy a condition:

.. code-block:: none

   [expression  for  item  in  iterable  if  condition]

The equivalent ``for`` loop is:

.. code-block:: python

   result = []
   for item in iterable:
       if condition:
           result.append(expression)

Example — keep only the even numbers from 0 to 19.  Run it and change the
condition:

.. try_examples::
   :height: 220px

   >>> evens = [n for n in range(20) if n % 2 == 0]
   >>> print(evens)
   [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

Example — extract only the vowels from a string:

.. try_examples::
   :height: 240px

   >>> s = "introduction"
   >>> vowels = [ch for ch in s if ch in "aeiou"]
   >>> print(vowels)
   ['i', 'o', 'u', 'i', 'o']

Comprehensions reward experimentation.  Change the expression, the
iterable, or the ``if`` condition and run again:

.. try_examples::
   :height: 300px

   >>> squares = [n ** 2 for n in range(1, 6)]
   >>> print(squares)
   [1, 4, 9, 16, 25]
   >>> evens = [n for n in range(20) if n % 2 == 0]
   >>> print(evens)
   [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
   >>> s = "introduction"
   >>> vowels = [ch for ch in s if ch in "aeiou"]
   >>> print(vowels)
   ['i', 'o', 'u', 'i', 'o']

Nested Comprehensions
---------------------

.. index:: list comprehension; nested

You can nest ``for`` clauses to iterate over two sequences simultaneously.
This produces a flat list — not a list of lists.  Run it live:

.. try_examples::
   :height: 220px

   >>> pairs = [(r, c) for r in range(3) for c in range(3)]
   >>> print(pairs)
   [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

The leftmost ``for`` is the outer loop; the rightmost is the inner loop —
the same order as nested ``for`` statements written out explicitly.

.. index:: list comprehension; when to use, side effects; avoid in comprehension

When to Use List Comprehensions
--------------------------------

Use a list comprehension when the goal is to *produce a list* from a
sequence.  Prefer a regular ``for`` loop when the body has side effects
(printing, writing a file, mutating external state) or when the logic is
complex enough that a one-liner hurts readability.

A good rule of thumb: if you can read the comprehension aloud as a single
English phrase — "the square of n for n in range 1 to 5" — it is probably
clear enough to use.
