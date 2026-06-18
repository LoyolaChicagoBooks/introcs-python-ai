.. index:: string; indexing, string; slicing

.. _string-indexing:

String Indexing and Slicing
============================

Strings are sequences of characters.  Python counts positions starting at
**0**, so the indices of the characters in ``"coding"`` are:

+-------------+-----+-----+-----+-----+-----+-----+
| Index       | 0   | 1   | 2   | 3   | 4   | 5   |
+-------------+-----+-----+-----+-----+-----+-----+
| Character   | c   | o   | d   | i   | n   | g   |
+-------------+-----+-----+-----+-----+-----+-----+

There are 6 characters and the last index is 5 — one less than the length.

.. warning::

   The last valid index is ``len(s) - 1``, not ``len(s)``.
   Accessing ``s[6]`` on a six-character string raises an ``IndexError``.

.. index:: string; subscript

Subscript Notation
------------------

Use square brackets to access a single character.  Press **Try it live** to
run these and change the index:

.. try_examples::
   :height: 280px

   >>> s = "coding"
   >>> s[0]
   'c'
   >>> s[2]
   'd'
   >>> s[5]
   'g'

The result is always a one-character string.

The subscript can be any expression that evaluates to an integer.  Try it live:

.. try_examples::
   :height: 220px

   >>> s = "coding"
   >>> n = 3
   >>> s[n - 1]
   'd'

.. index:: string; negative index

Negative Indices
----------------

Python allows *negative* indices that count from the right end.  Try it live:

.. try_examples::
   :height: 260px

   >>> s = "coding"
   >>> s[-1]     # last character
   'g'
   >>> s[-2]     # second from last
   'n'
   >>> s[-6]     # same as s[0]
   'c'

``s[-1]`` is equivalent to ``s[len(s) - 1]``.

.. index:: string; slice, slice notation

Slicing
-------

A *slice* extracts a substring using the notation ``s[start:stop]``.
The result includes characters from index ``start`` up to, **but not
including**, index ``stop``.  Try it live:

.. try_examples::
   :height: 220px

   >>> s = "coding"
   >>> s[1:4]
   'odi'
   >>> s[0:3]
   'cod'

Omitting either end uses the beginning or end of the string.  Try it live:

.. try_examples::
   :height: 260px

   >>> s = "coding"
   >>> s[:3]     # from the start
   'cod'
   >>> s[3:]     # to the end
   'ing'
   >>> s[:]      # whole string (copy)
   'coding'

Slices work with negative indices too.  Try it live:

.. try_examples::
   :height: 240px

   >>> s = "coding"
   >>> s[-3:]    # last three characters
   'ing'
   >>> s[:-2]    # everything except the last two
   'codi'

.. index:: string; step in slice

Step in Slices
--------------

An optional third number specifies a *step*.  Try it live:

.. try_examples::
   :height: 240px

   >>> s = "abcdefgh"
   >>> s[::2]       # every other character
   'aceg'
   >>> s[::-1]      # reverse the string
   'hgfedcba'

Reversing with ``[::-1]`` is an idiomatic Python trick worth remembering.

Indexing Exercise
-----------------

Predict what each line prints, then run the cell to check your predictions.
Experiment with your own slices — try different ``start``, ``stop``, and
``step`` values:

.. try_examples::
   :height: 320px

   >>> s = "fragment"
   >>> k = 3
   >>> print(s[1])
   r
   >>> print(s[k])
   g
   >>> print(s[2 * k - 2])
   m
   >>> print(s[-1])
   t
   >>> print(s[2:5])
   agm
   >>> print(s[::-1])      # reversed
   tnemgarf
