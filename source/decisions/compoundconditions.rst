.. index:: and, or, not, Boolean operators, compound condition

Compound Boolean Expressions
=============================

Simple comparisons test one thing at a time.  Often we need to combine
conditions: "the temperature is above 70 *and* it is not raining."
Python uses the keywords ``and``, ``or``, and ``not``.

.. index:: and operator

``and``
-------

``a and b`` is ``True`` only when *both* ``a`` and ``b`` are true.  Try it live:

.. try_examples::
   :height: 240px

   >>> x = 5
   >>> x > 0 and x < 10
   True
   >>> x > 0 and x > 10
   False

.. index:: or operator

``or``
------

``a or b`` is ``True`` when *at least one* of ``a`` or ``b`` is true.  Try it live:

.. try_examples::
   :height: 240px

   >>> x = 15
   >>> x < 0 or x > 10
   True
   >>> x < 0 or x > 20
   False

.. index:: not operator

``not``
-------

``not a`` flips the truth value.  Try it live:

.. try_examples::
   :height: 260px

   >>> not True
   False
   >>> not False
   True
   >>> x = 5
   >>> not (x > 10)
   True

.. index:: truth table

Truth Tables
------------

+-------+-------+---------------+--------------+-----------+
| ``a`` | ``b`` | ``a and b``   | ``a or b``   | ``not a`` |
+=======+=======+===============+==============+===========+
| True  | True  | True          | True         | False     |
+-------+-------+---------------+--------------+-----------+
| True  | False | False         | True         | False     |
+-------+-------+---------------+--------------+-----------+
| False | True  | False         | True         | True      |
+-------+-------+---------------+--------------+-----------+
| False | False | False         | False        | True      |
+-------+-------+---------------+--------------+-----------+

.. index:: Boolean operators; precedence

Operator Precedence
-------------------

Among Boolean operators, ``not`` has the highest precedence, then ``and``,
then ``or``.  Comparison operators (``<``, ``==``, etc.) have higher
precedence than all three.  So this expression:

.. code-block:: python

   x > 0 and x < 10 or y == 5

is parsed as:

.. code-block:: python

   (x > 0 and x < 10) or (y == 5)

Use parentheses when in doubt — they make intent clear.

.. index:: short-circuit evaluation

Short-Circuit Evaluation
------------------------

Python evaluates ``and`` and ``or`` *lazily*: it stops as soon as the
result is determined.

- ``a and b``: if ``a`` is false, ``b`` is never evaluated.
- ``a or b``: if ``a`` is true, ``b`` is never evaluated.

This is called *short-circuit evaluation*.  It lets you write safe checks
like:

.. code-block:: python

   if s and s[0] == 'A':
       print("starts with A")

If ``s`` is an empty string, ``s`` is falsy, so ``s[0]`` is never
evaluated — avoiding an ``IndexError``.

Common Patterns
---------------

Check if a value is in a numeric range:

.. code-block:: python

   if 0 <= score <= 100:
       print("valid score")

Test for two possible values:

.. code-block:: python

   if answer == "yes" or answer == "y":
       print("confirmed")

Negate a condition:

.. code-block:: python

   if not name.startswith("Dr."):
       name = "Dr. " + name
