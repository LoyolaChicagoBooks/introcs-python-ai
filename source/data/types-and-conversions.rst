.. index:: types, type conversion

Types and Conversions
=====================

Every value in Python has a *type* that determines what operations can be
performed on it and how it is stored.

.. index:: built-in types

Built-in Types
--------------

The four types used most often in early programs are:

``int``
   Whole numbers: ``0``, ``42``, ``-17``, ``1_000_000``.

``float``
   Approximate real numbers: ``3.14``, ``-0.5``, ``2.0``, ``1.5e3``.

``str``
   Strings of characters: ``"Hello"``, ``'Python'``, ``"42"``.

``bool``
   Boolean truth values: ``True`` or ``False``.

Use ``type()`` to see the type of any value.  Try it in the cell below:

.. try_examples::
   :height: 260px

   >>> type(42)
   <class 'int'>
   >>> type(3.14)
   <class 'float'>
   >>> type("Hello")
   <class 'str'>
   >>> type(True)
   <class 'bool'>

.. index:: type conversion functions

Type Conversion
---------------

Use the type name as a function to convert between types:

.. list-table::
   :header-rows: 1
   :widths: 15 40 30

   * - Function
     - Description
     - Example
   * - ``int(x)``
     - Convert to integer (truncates floats)
     - ``int(3.9)`` → ``3``
   * - ``float(x)``
     - Convert to float
     - ``float(7)`` → ``7.0``
   * - ``str(x)``
     - Convert to string
     - ``str(42)`` → ``"42"``
   * - ``bool(x)``
     - Convert to bool
     - ``bool(0)`` → ``False``

.. try_examples::
   :height: 300px

   >>> int("42")        # str -> int
   42
   >>> float("3.14")    # str -> float
   3.14
   >>> int(3.99)        # float -> int (truncates toward zero)
   3
   >>> str(100)         # int -> str
   '100'
   >>> round(3.99)      # rounds instead of truncating
   4

.. index:: int(); truncation, truncation vs rounding

Note that ``int()`` *truncates* floats toward zero — it does not round.  See
for yourself:

.. try_examples::
   :height: 220px

   >>> int(3.9)
   3
   >>> int(-3.9)
   -3

Use ``round()`` if you need rounding.  Edit the values in the cell above, and
try converting a string that is *not* a number (for example ``int("hello")``)
to see the ``ValueError`` Python raises.

.. index:: bool, truthiness

Boolean Values and Truthiness
------------------------------

``True`` and ``False`` are the two boolean values.  Every Python value can be
interpreted as boolean in a condition:

- **Falsy values:** ``0``, ``0.0``, ``""`` (empty string), ``[]`` (empty list),
  ``{}`` (empty dict), ``None``
- **Truthy values:** everything else

Run these conversions to see truthiness in action:

.. try_examples::
   :height: 260px

   >>> bool(0)
   False
   >>> bool(1)
   True
   >>> bool("")
   False
   >>> bool("hello")
   True

.. index:: None

None
----

``None`` is a special value that represents the *absence* of a value.  It is
Python's equivalent of null.  Try assigning and testing it:

.. try_examples::
   :height: 240px

   >>> x = None
   >>> x is None
   True
   >>> print(x)
   None

Functions that do not explicitly return a value return ``None`` automatically.
``None`` is also used as a placeholder when a variable exists but has not been
given a meaningful value yet.

.. index:: None; is None, identity test

Test for ``None`` with ``is None``, not with ``== None``:

.. code-block:: python

   if result is None:
       print("No result yet.")
