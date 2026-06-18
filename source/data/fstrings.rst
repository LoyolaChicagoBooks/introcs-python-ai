.. index:: f-string, format string
   ACM-IEEE CS2013; AR2 Machine Level Representation of Data
   ACM-IEEE CS2023; AR2 Machine Level Representation of Data

.. _fstrings:

F-Strings and String Formatting
================================


Combining strings with variable values is one of the most common tasks in a
program.  Python's *f-strings* (formatted string literals) are the modern,
readable way to do it.

.. index:: f-string; basic syntax

Basic F-Strings
---------------

An f-string is a string literal prefixed with ``f`` (or ``F``).  Inside the
string, any expression enclosed in curly braces ``{}`` is evaluated and its
value is inserted.  Any Python expression can go inside ``{}``.  Press
**Try it live** and edit the names, ages, and expressions:

.. try_examples::
   :height: 300px

   >>> name = "Alice"
   >>> age = 20
   >>> print(f"My name is {name} and I am {age} years old.")
   My name is Alice and I am 20 years old.
   >>> x = 5
   >>> print(f"The square of {x} is {x ** 2}.")
   The square of 5 is 25.
   >>> a, b = 3, 4
   >>> print(f"The hypotenuse is {(a**2 + b**2) ** 0.5:.2f}.")
   The hypotenuse is 5.00.

.. index:: format specifier

Format Specifiers
-----------------

After the expression you can add a *format specifier* separated by a colon to
control how the value is displayed.

**Floating-point precision:** press **Try it live** and change the precision:

.. try_examples::
   :height: 240px

   >>> pi = 3.141592653589793
   >>> print(f"pi ≈ {pi:.4f}")
   pi ≈ 3.1416
   >>> price = 9.5
   >>> print(f"Price: ${price:.2f}")
   Price: $9.50

.. index:: f-string; field width, f-string; alignment

**Field width and alignment:** press **Try it live** and try the alignment
specifiers in the comments below:

.. try_examples::
   :height: 240px

   >>> for i in range(1, 4):
   ...     print(f"{i:3}  {i**2:5}")
   ...
     1      1
     2      4
     3      9

- ``:3`` means: right-align in a field of width 3.
- ``:<10`` means: left-align in a field of width 10.
- ``:^10`` means: center in a field of width 10.

.. index:: f-string; integer format, f-string; binary, f-string; hexadecimal

**Integer formatting:** format specifiers are easiest to learn by experiment.
Press **Try it live** and change the values and the specifiers:

.. try_examples::
   :height: 300px

   >>> n = 255
   >>> print(f"{n:d}")       # decimal
   255
   >>> print(f"{n:08b}")     # binary, zero-padded to 8 digits
   11111111
   >>> print(f"{n:x}")       # hexadecimal
   ff
   >>> print(f"{n:#x}")      # hexadecimal with 0x prefix
   0xff
   >>> pi = 3.141592653589793
   >>> print(f"pi to 4 places: {pi:.4f}")
   pi to 4 places: 3.1416

.. index:: str.format()

Older Formatting Methods
------------------------

You may encounter two older formatting styles in existing code.

*The* ``.format()`` *method:*

.. code-block:: python

   print("The wall area is {} square feet.".format(wall_area))
   print("Name: {0}, Age: {1}".format(name, age))

*Percent-style formatting* is the oldest style; press **Try it live** to run it:

.. try_examples::
   :height: 220px

   >>> print("pi = %.4f" % 3.14159)
   pi = 3.1416

F-strings are preferred in new code because they are more readable and
slightly faster.

The Painting Program Revisited
-------------------------------

Here is the output section of the painting program using f-strings:

.. code-block:: python

   print(f"The wall area is {wall_area} square feet.")
   print(f"The ceiling area is {ceiling_area} square feet.")

To display the areas with exactly one decimal place:

.. code-block:: python

   print(f"The wall area is {wall_area:.1f} square feet.")
   print(f"The ceiling area is {ceiling_area:.1f} square feet.")
