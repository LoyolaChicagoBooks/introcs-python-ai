.. index:: arithmetic

.. _arithmetic:

Arithmetic
==========

We start with integers and arithmetic — not because arithmetic is exciting, but
because the symbolism should be mostly familiar.

.. index:: Python; interactive shell
   REPL

Testing Expressions in the Shell
---------------------------------

Python's interactive shell is perfect for trying out arithmetic.  Start it
with ``python3`` and type expressions at the ``>>>`` prompt.  Press **Try it
live** to evaluate these expressions and edit the numbers — if this is the first
one you have seen, :ref:`here is how it works <try-it-live>`:

.. try_examples::
   :height: 220px

   >>> 2 + 3
   5
   >>> 10 - 4
   6
   >>> 3 * 7
   21

The shell evaluates the expression and prints the result immediately.  This
is much faster than writing a whole program for small experiments.

.. index:: integer, float

Numeric Types
-------------

Python has two main numeric types for beginners:

``int``
   Whole numbers, positive or negative, with no fractional part:
   ``0``, ``42``, ``-17``, ``1000000``.

   Python integers have *unlimited precision* — they can be as large as
   your computer's memory allows.  There is no overflow.

``float``
   Approximate real numbers, written with a decimal point or an exponent:
   ``.2``, ``2.0``, ``20.``, ``2000e-1``, ``2E3``.

The built-in ``type`` function reports the type of any value.  Try it live and
check the type of a few values of your own:

.. try_examples::
   :height: 220px

   >>> type(42)
   <class 'int'>
   >>> type(3.14)
   <class 'float'>

.. index:: operator; arithmetic

Arithmetic Operators
--------------------

The arithmetic operators in Python are:

.. list-table::
   :header-rows: 1
   :widths: 15 20 40

   * - Operator
     - Meaning
     - Example
   * - ``+``
     - Addition
     - ``3 + 4`` → ``7``
   * - ``-``
     - Subtraction
     - ``10 - 3`` → ``7``
   * - ``*``
     - Multiplication
     - ``3 * 4`` → ``12``
   * - ``/``
     - Division (always float)
     - ``7 / 2`` → ``3.5``
   * - ``//``
     - Floor division (integer result)
     - ``7 // 2`` → ``3``
   * - ``%``
     - Remainder (modulus)
     - ``7 % 2`` → ``1``
   * - ``**``
     - Exponentiation
     - ``2 ** 10`` → ``1024``
   * - ``-x``
     - Negation (unary)
     - ``-5``

.. index:: operator; /; true division, operator; //; floor division, operator; %; modulus, operator; **; exponentiation

A key difference from many other languages: ``/`` *always* produces a
``float``, even if both operands are integers.  Use ``//`` when you want a
whole-number result.  Press **Try it live** to run these and edit the numbers:

.. try_examples::
   :height: 280px

   >>> 7 / 2      # true division -> always a float
   3.5
   >>> 6 / 2
   3.0
   >>> 7 // 2     # floor division -> int
   3
   >>> -7 // 2
   -4
   >>> 7 % 2      # remainder (modulus)
   1
   >>> 2 ** 10    # exponentiation
   1024

.. index:: operator precedence

Operator Precedence
-------------------

Python follows the standard mathematical order of operations.  From highest
to lowest precedence:

1. ``**`` (exponentiation, right to left)
2. ``-x`` (unary negation)
3. ``*``, ``/``, ``//``, ``%`` (multiplication and division)
4. ``+``, ``-`` (addition and subtraction)

Use parentheses to override the default order.  Try it live and see how the
parentheses change the result:

.. try_examples::
   :height: 220px

   >>> 2 + 3 * 4
   14
   >>> (2 + 3) * 4
   20

See the appendix for the complete precedence table.

.. index:: mixed arithmetic, type conversion

Mixed Arithmetic
----------------

When you mix ``int`` and ``float`` in an expression, Python converts the
``int`` to ``float`` automatically.  Try it live and watch how the result type
changes:

.. try_examples::
   :height: 240px

   >>> 1 + 2.0
   3.0
   >>> type(1 + 2)
   <class 'int'>
   >>> type(1 + 2.0)
   <class 'float'>

.. index:: widening conversion, implicit type conversion

This *widening* conversion preserves the value.

.. index:: built-in functions; abs, round, divmod

Useful Built-in Functions
--------------------------

Python provides several useful arithmetic functions built in — no import
needed:

.. list-table::
   :header-rows: 1
   :widths: 20 50

   * - Function
     - Description
   * - ``abs(x)``
     - Absolute value of ``x``
   * - ``round(x)``
     - Round to nearest integer
   * - ``round(x, n)``
     - Round to ``n`` decimal places
   * - ``divmod(x, y)``
     - Returns ``(x // y, x % y)`` as a tuple
   * - ``pow(x, y)``
     - ``x ** y``  (also ``pow(x, y, z)`` for modular exponentiation)
   * - ``max(a, b, ...)``
     - Largest value
   * - ``min(a, b, ...)``
     - Smallest value

Try these built-in functions live and edit the arguments:

.. try_examples::
   :height: 240px

   >>> abs(-7)
   7
   >>> round(3.14159, 2)
   3.14
   >>> divmod(17, 5)
   (3, 2)

.. index:: math module, math.sqrt(), math.floor(), math.ceil(), math.pi

The ``math`` module provides more functions.  Import it first, then try it live:

.. try_examples::
   :height: 280px

   >>> import math
   >>> math.sqrt(2)
   1.4142135623730951
   >>> math.pi
   3.141592653589793
   >>> math.floor(3.7)
   3
   >>> math.ceil(3.2)
   4
