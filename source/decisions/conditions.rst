.. index:: Boolean, bool, True, False
   ACM-IEEE CS2013; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2023; SDF2 Fundamental Programming Concepts

.. _Simple-Conditions:

Conditions
==========

So far all our programs have executed instructions sequentially.  But many
problems require making a *decision*: do one thing if some condition is true,
something else otherwise.

A *condition* is an expression whose value is either ``True`` or ``False``.
These are Python's *Boolean* values (named after 19th-century mathematician
George Boole), and their type is ``bool``.  Press **Try it live** to evaluate
these comparisons and edit the numbers:

.. try_examples::
   :height: 280px

   >>> 2 < 5
   True
   >>> 3 > 7
   False
   >>> x = 11
   >>> x > 10
   True
   >>> 2 * x < x
   False

.. index:: comparison operators; ==, !=, <, >, <=, >=

Comparison Operators
--------------------

The basic comparison operators that produce Boolean results are:

.. list-table::
   :header-rows: 1
   :widths: 15 40

   * - Operator
     - Meaning
   * - ``==``
     - Equal to
   * - ``!=``
     - Not equal to
   * - ``<``
     - Less than
   * - ``>``
     - Greater than
   * - ``<=``
     - Less than or equal to
   * - ``>=``
     - Greater than or equal to

.. warning::

   Use ``==`` for comparison, ``=`` for assignment.  Writing ``if x = 5:``
   is a ``SyntaxError`` in Python.

.. index:: bool type, True, False, falsy values, truthy values

The ``bool`` Type
-----------------

``True`` and ``False`` are built-in constants, not strings.  You can also
create Boolean values with the ``bool()`` conversion function.  Try it live:

.. try_examples::
   :height: 280px

   >>> bool(0)
   False
   >>> bool(1)
   True
   >>> bool("")
   False
   >>> bool("hello")
   True

Any non-zero number and any non-empty sequence is *truthy*; zero, ``None``,
and empty sequences are *falsy*.  This matters in ``if`` statements.

.. index:: chained comparison; conditions

Chained Comparisons
-------------------

Python allows comparisons to be *chained*.  Try it live:

.. try_examples::
   :height: 220px

   >>> x = 5
   >>> 0 < x < 10
   True
   >>> 0 < x < 4
   False

The expression ``0 < x < 10`` is equivalent to ``0 < x and x < 10``.
Chaining reads naturally and avoids repeating the middle variable.
