.. index:: variable; assignment
   assignment statement
   ACM-IEEE CS2013; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2023; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2013; PL4 Basic Type Systems
   ACM-IEEE CS2023; PL4 Basic Type Systems

.. _Variables-and-Assignment:

Variables and Assignment
=========================

Programs need to store and refer to data.  *Variables* are names that refer
to values stored in memory.

.. index:: assignment; no declaration needed

No Declarations Needed
----------------------

In Python, you simply assign a value.  The variable is created automatically
and takes the type of whatever you assign to it.  Press **Try it live** to run
these statements yourself:

.. try_examples::
   :height: 300px

   >>> width = 5.0
   >>> width
   5.0

   The *value* has a type; the *variable* does not.  You can assign a different
   type to the same variable name later (though this is rarely a good idea):

   >>> x = 10
   >>> type(x)
   <class 'int'>
   >>> x = 3.14
   >>> type(x)
   <class 'float'>

.. index:: assignment statement; right-to-left

Assignment is Right-to-Left
-----------------------------

An assignment statement evaluates the expression on the *right* side first,
then stores the result in the variable on the *left*.  Try it yourself:

.. try_examples::
   :height: 280px

   >>> area = 5 * 7
   >>> area
   35

   The variable on the left receives the result.  This works even when the same
   variable appears on both sides:

   >>> n = 3
   >>> n = n + 1
   >>> n
   4

The right side is evaluated first (``n + 1`` = 4), then that value replaces
the old value of ``n``.  This is *not* a mathematical equation — it is an
instruction to update a stored value.

.. index:: identifier, naming conventions, snake_case

Naming Rules and Conventions
-----------------------------

Variable names (called *identifiers*) must:

- Start with a letter or underscore (``_``).
- Contain only letters, digits, and underscores.
- Not be a Python keyword (like ``if``, ``for``, ``while``, ``def``).

Python is *case-sensitive*: ``total``, ``Total``, and ``TOTAL`` are three
different variables.

**Convention:** Use ``snake_case`` for variable names — all lowercase with
underscores between words:

.. code-block:: python

   wall_area = 488.0
   room_length = 20.5
   student_count = 30

By convention, names written in ALL_CAPS indicate constants — values that are
not intended to change:

.. code-block:: python

   HEIGHT = 8
   PI = 3.14159

Python does not enforce this convention, but it is widely followed and helps
readers understand your program.

.. index:: multiple assignment, augmented assignment

Multiple and Augmented Assignment
-----------------------------------

You can assign the same value to several variables at once, and you can also
assign to multiple variables from multiple values in one line.  Try it:

.. try_examples::
   :height: 320px

   >>> i = j = 0
   >>> i
   0
   >>> j
   0

   You can also assign to multiple variables from multiple values in one line:

   >>> x, y = 3, 4
   >>> x
   3
   >>> y
   4

.. index:: tuple unpacking; preview, multiple assignment; simultaneous

This is called *tuple unpacking* (discussed further in the Tuples chapter).
A particularly elegant use is swapping two values without a temporary variable.
Run it to see the values exchange:

.. try_examples::
   :height: 260px

   >>> a, b = 10, 20
   >>> a, b = b, a
   >>> a
   20
   >>> b
   10

.. index:: augmented assignment; operators list, +=, -=, *=, /=, //=, %=, **=

*Augmented assignment* operators combine an operation with assignment.  Try
stepping through these updates:

.. try_examples::
   :height: 260px

   >>> n = 5
   >>> n += 3     # same as n = n + 3
   >>> n
   8
   >>> n *= 2     # same as n = n * 2
   >>> n
   16

The operators ``+=``, ``-=``, ``*=``, ``/=``, ``//=``, ``%=``, and ``**=``
all work the same way.

Exercises
---------

*Think* what the printed result would be, then press **Try it live** to check.
Try rewriting the reassignments using augmented operators such as ``+=`` and
``*=``:

.. try_examples::
   :height: 280px

   >>> x = 1
   >>> x = x + 1
   >>> x = x * 3
   >>> x = x * 5
   >>> print(x)
   30

Another to try:

.. try_examples::
   :height: 280px

   >>> a = 5
   >>> a = a // 2
   >>> a = a + 1
   >>> a = a * 2
   >>> print(a)
   6
