.. index:: for loop; examples, example; for loop

.. _For-Examples:

For Loop Examples
=================

Multiples of k
--------------

.. index:: multiples example

Suppose we want to print the first ``n`` multiples of ``k`` — for example
the first 5 multiples of 3: 3, 6, 9, 12, 15.

One approach uses an index 1 through ``n`` and multiplies.  Press **Try it
live** to run it and change ``n`` or ``k``:

.. try_examples::
   :height: 260px

   >>> n, k = 5, 3
   >>> for i in range(1, n + 1):
   ...     print(i * k)
   ...
   3
   6
   9
   12
   15

.. index:: range(); custom step

Another approach steps directly through the multiples using a custom step:

.. try_examples::
   :height: 260px

   >>> n, k = 5, 3
   >>> for i in range(k, n * k + 1, k):
   ...     print(i)
   ...
   3
   6
   9
   12
   15

Both produce identical output.  The second is natural when the step size
*is* the value you care about.

Compound Assignment Operators
------------------------------

.. index:: operator; +=, operator; -=, operator; *=, operator; //=, operator; %=

Python supports shorthand assignment operators.  For any
binary operator *op*, ``x op= expr`` means ``x = x op expr``:

- ``x += 5``  is the same as  ``x = x + 5``
- ``x -= 3``  is the same as  ``x = x - 3``
- ``x *= 2``  is the same as  ``x = x * 2``
- ``x //= 4`` is the same as  ``x = x // 4``   (integer division)
- ``x %= 7``  is the same as  ``x = x % 7``

.. _power_table:

Tables
------

.. index:: table formatting, f-string; field width, example; power table

Reports often display data in aligned columns.  As a first table, print
the square, cube, and square root of integers 1 through 10.

A first attempt without any formatting:

.. code-block:: python

   import math

   for n in range(1, 11):
       print(n, n**2, n**3, math.sqrt(n))

Output:

.. code-block:: none

   1 1 1 1.0
   2 4 8 1.4142135623730951
   3 9 27 1.7320508075688772
   ...
   10 100 1000 3.1622776601683795

The numbers are correct but the columns are ragged.  Python f-strings let
us specify field widths and precision.  The format spec ``{value:Nd}``
right-justifies an integer in a field of width N; ``{value:N.4f}`` gives
a float with 4 decimal places in a field of width N.  Run it and try
adjusting the widths:

.. try_examples::
   :height: 360px

   >>> import math
   >>> print(f"{'n':>4} {'square':>8} {'cube':>8} {'root':>8}")
      n   square     cube     root
   >>> for n in range(1, 11):
   ...     print(f"{n:4d} {n**2:8d} {n**3:8d} {math.sqrt(n):8.4f}")
   ...
      1        1        1   1.0000
      2        4        8   1.4142
      3        9       27   1.7321
      4       16       64   2.0000
      5       25      125   2.2361
      6       36      216   2.4495
      7       49      343   2.6458
      8       64      512   2.8284
      9       81      729   3.0000
     10      100     1000   3.1623

The heading uses the same field widths as the data rows so that the
columns line up.

.. _ASCII-table:

ASCII and Character Codes
--------------------------

.. index:: ASCII, ord(), chr(), character codes

Every character has a numeric code.  Python's ``ord(ch)`` returns the
integer code of character ``ch``; ``chr(i)`` does the reverse.  Codes
32 through 126 correspond to the printable characters on a US keyboard.

A simple listing, one per line:

.. code-block:: python

   for i in range(32, 127):
       print(f"{i:3d} {chr(i)}")

To save space, we can print 8 entries per line.  We stay on the same line
with ``print(..., end="  ")`` and advance to the next line after every 8th
entry (when ``i % 8 == 7``):

.. code-block:: python

   for i in range(32, 127):
       print(f"{i:3d} {chr(i)}", end="  ")
       if i % 8 == 7:
           print()
   print()

The final ``print()`` ensures the last (partial) line is terminated.

.. _mod-mult-table:

Modular Multiplication Table
-----------------------------

.. index:: nested loop; table, modular arithmetic, example; mod table

Modular arithmetic takes remainders after multiplying.  For example,
3 × 5 mod 7 = 15 % 7 = 1.  We will print the full multiplication table
mod 7 — a useful structure in cryptography.

Our target output:

.. code-block:: none

   * | 0 1 2 3 4 5 6
   -----------------
   0 | 0 0 0 0 0 0 0
   1 | 0 1 2 3 4 5 6
   2 | 0 2 4 6 1 3 5
   3 | 0 3 6 2 5 1 4
   4 | 0 4 1 5 2 6 3
   5 | 0 5 3 1 6 4 2
   6 | 0 6 5 4 3 2 1

Start with pseudocode — one row per value of ``r``:

.. code-block:: none

   for r in range(7):
       print row r

Each row is itself a repetitive pattern — columns 0 through 6 — so we
replace "print row r" with an inner loop:

.. code-block:: none

   for r in range(7):
       for c in range(7):
           print (r * c) % 7, stay on same line
       advance to next line

Translating to Python:

.. code-block:: python

   for r in range(7):
       for c in range(7):
           print((r * c) % 7, end=" ")
       print()

This gets the body right.  Now add the border labels.  The heading row
prints ``"* |"`` once, then the column labels 0–6:

.. code-block:: python

   print("* |", end=" ")
   for i in range(7):
       print(i, end=" ")
   print()
   print("-" * 17)

   for r in range(7):
       print(f"{r} |", end=" ")
       for c in range(7):
           print((r * c) % 7, end=" ")
       print()

To generalise to mod ``n``, replace 7 with ``n`` and compute the column
width from the number of digits in ``n``:

.. literalinclude:: ../../examples/introcs-python/for/mod_table.py
   :language: python
   :start-after: # start: mod_mult_table
   :end-before: # end: mod_mult_table

.. code-block:: python

   mod_mult_table(7)

Output:

.. code-block:: none

   * | 0 1 2 3 4 5 6
   -----------------
   0 | 0 0 0 0 0 0 0
   1 | 0 1 2 3 4 5 6
   2 | 0 2 4 6 1 3 5
   3 | 0 3 6 2 5 1 4
   4 | 0 4 1 5 2 6 3
   5 | 0 5 3 1 6 4 2
   6 | 0 6 5 4 3 2 1

.. _reversed-string:

Reversed String
---------------

.. index:: string; reverse, accumulation pattern

To reverse a string we iterate through it backwards and accumulate
characters.  Start ``rev`` as the empty string and append each character.
Run it and try reversing a word of your own:

.. try_examples::
   :height: 240px

   >>> def reversed_string(s: str) -> str:
   ...     rev = ""
   ...     for i in range(len(s) - 1, -1, -1):
   ...         rev += s[i]
   ...     return rev
   ...
   >>> print(reversed_string("drab"))
   bard

Trace through ``"drab"`` to confirm: the loop visits indices 3, 2, 1, 0,
producing characters ``'b'``, ``'a'``, ``'r'``, ``'d'``, which accumulate
as ``"b"``, ``"ba"``, ``"bar"``, ``"bard"``.

Python also offers a concise built-in idiom for the same result:

.. code-block:: python

   s[::-1]   # slice with step -1 reverses the string

Understanding the explicit loop version first makes the slice idiom easier
to trust.

Using ``enumerate()``
----------------------

.. index:: enumerate()

Sometimes you need both the *position* and the *value* while iterating.
Python's ``enumerate()`` provides both without manual index tracking.  Run
it live:

.. try_examples::
   :height: 240px

   >>> words = ["apple", "banana", "cherry"]
   >>> for i, word in enumerate(words):
   ...     print(f"{i}: {word}")
   ...
   0: apple
   1: banana
   2: cherry

``enumerate()`` returns pairs ``(index, item)``; the ``for`` loop unpacks
each pair into ``i`` and ``word``.  An optional second argument sets the
starting index:

.. try_examples::
   :height: 240px

   >>> words = ["apple", "banana", "cherry"]
   >>> for i, word in enumerate(words, start=1):
   ...     print(f"{i}. {word}")
   ...
   1. apple
   2. banana
   3. cherry

This is cleaner than the while-loop alternative of maintaining a separate
counter variable.
