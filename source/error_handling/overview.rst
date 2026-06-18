.. index:: error handling, exceptions, try, except, finally, raise, ValueError, ZeroDivisionError
   ACM-IEEE CS2013; SDF4 Development Methods
   ACM-IEEE CS2023; SDF4 Development Methods

.. _Error-Handling:

Error Handling
==============

.. note::
   *Source:* Contributed by PhD students in COMP 501 at Loyola University Chicago.

Errors are a normal part of programming. Python distinguishes between three
categories of errors, each requiring a different response.

.. index:: syntax error, runtime error; exception, logic error; debugging

Types of Errors
---------------

+-------------------+-----------------------------+---------------------------------------+
| Category          | Example                     | Fix                                   |
+===================+=============================+=======================================+
| **Syntax error**  | ``if x > 3 print(x)``       | Read the message and correct the code |
|                   |                             | before running.                       |
+-------------------+-----------------------------+---------------------------------------+
| **Runtime error** | ``1 / 0``                   | Catch with ``try``/``except``.        |
+-------------------+-----------------------------+---------------------------------------+
| **Logic error**   | Wrong output for valid input| Test with known inputs; add print     |
|                   |                             | statements to trace values.           |
+-------------------+-----------------------------+---------------------------------------+

A **syntax error** is caught by Python before the program runs. A **runtime error**
(also called an *exception*) occurs while the program is running and, if unhandled,
crashes it. A **logic error** produces incorrect results without crashing —
these are the hardest to find.

.. index:: try/except; basic pattern, except; clause ordering, else; try block, finally; cleanup

Basic Exception Handling
------------------------

Python's ``try``/``except`` block lets you catch runtime errors and respond to them
gracefully instead of crashing.

.. code-block:: python

   try:
       x = int(input("Enter a number: "))
       print(10 / x)
   except ValueError:
       print("Please enter numbers only.")
   except ZeroDivisionError:
       print("Cannot divide by zero.")
   else:
       print("Success!")
   finally:
       print("Done.")

- ``except`` blocks are checked in order — the first match wins, so put specific
  exceptions before general ones.
- ``else`` runs only if the ``try`` block completed without raising an exception.
- ``finally`` always runs, whether or not an exception occurred. Use it for
  clean-up (closing files, releasing resources).

.. index:: ValueError, ZeroDivisionError, FileNotFoundError, TypeError, KeyError, IndexError

Common Exception Types
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Exception
     - When it occurs
   * - ``ValueError``
     - Argument has the right type but an invalid value (e.g., ``int("abc")``).
   * - ``ZeroDivisionError``
     - Division or modulo by zero.
   * - ``FileNotFoundError``
     - File or directory does not exist.
   * - ``TypeError``
     - Operation applied to an object of the wrong type.
   * - ``KeyError``
     - Dictionary key not found.
   * - ``IndexError``
     - List index out of range.

.. index:: FileNotFoundError; catching, exception; as clause, open(); exception handling

Catching File Errors
--------------------

File operations frequently raise exceptions. Wrapping them in ``try``/``except``
makes programs robust:

.. code-block:: python

   try:
       with open("data.txt") as f:
           print(f.read())
   except FileNotFoundError as e:
       print("File not found:", e)

The ``as e`` clause binds the exception object to the variable ``e``, giving you
access to the error message.

.. index:: exception; inside a loop, try/except; in loop, skip invalid items

Handling Errors Inside a Loop
------------------------------

When processing a collection, you often want to skip invalid items rather than
aborting the entire program. Run this and try changing the values in ``nums``:

.. try_examples::
   :height: 280

   >>> nums = ["1", "2", "three", "4"]
   >>> total = 0
   >>> for n in nums:
   ...     try:
   ...         total += int(n)
   ...     except ValueError:
   ...         print(f"Skipped bad value: {n}")
   ...
   Skipped bad value: three
   >>> print("Total:", total)
   Total: 7

.. index:: raise statement, exception; raising deliberately

Raising Exceptions
------------------

You can raise exceptions deliberately using ``raise`` to signal that something is
wrong:

.. literalinclude:: ../../examples/introcs-python/error_handling/safe_divide.py
   :language: python
   :start-after: # start: safe_divide
   :end-before: # end: safe_divide

Output:

.. code-block:: none

   Cannot divide by zero.

.. index:: EAFP style; Python, LBYL style, exception; prevention vs catching

Prevention vs. Catching
-----------------------

There are two philosophies for dealing with potential errors:

- **Prevention** — check conditions before they cause problems (``if``/``else``).
- **Catching** — let the error occur and handle it in an ``except`` block.

Python generally favors the "easier to ask forgiveness than permission" (EAFP) style
— try the operation and handle exceptions if they arise, rather than checking every
precondition. This makes code more readable and avoids race conditions when checking
and acting on a condition separately.

However, some checks are better done upfront. Validating user input before
processing it is cleaner than catching errors deep in the call stack.

Exercises
---------

1. Write a function ``safe_divide(a, b)`` that returns ``a / b`` or ``None`` if
   division is not possible, printing a helpful message in either error case.
   Test it with ``(4, 2)``, ``(5, 0)``, and ``("x", 2)``.
2. Open a file called ``numbers.txt`` where each line contains one value. Sum all
   valid integers and skip lines that are not valid integers. Use ``raise
   ValueError`` if the file is completely empty.
3. What is the difference between *detecting* an error and *handling* it? Give an
   example of each.
4. Modify exercise 2 so that invalid lines are written to ``error_log.txt`` instead
   of printed to the screen.
5. Research the ``assert`` statement. Write two assertions that guard a function
   against invalid inputs.
