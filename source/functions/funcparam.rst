.. index:: function; parameter

Function Parameters
===================

The two birthday functions in the previous section were nearly identical.  The
only difference was the name.  *Parameters* let us pass data into a function,
eliminating duplication.

.. index:: parameter, argument

Defining a Parameter
---------------------

Add a parameter name inside the parentheses of the ``def`` line:

.. code-block:: python

   def happy_birthday(person):
       print("Happy Birthday to you!")
       print("Happy Birthday to you!")
       print(f"Happy Birthday, dear {person}.")
       print("Happy Birthday to you!")

The parameter ``person`` is a local variable that receives a value when the
function is called.

Calling with an Argument
------------------------

When you call a function with a parameter, you supply an *argument* — the
value to pass in:

.. try_examples::
   :height: 300px

   >>> def happy_birthday(person):
   ...     print("Happy Birthday to you!")
   ...     print("Happy Birthday to you!")
   ...     print(f"Happy Birthday, dear {person}.")
   ...     print("Happy Birthday to you!")
   ...
   >>> happy_birthday("Emily")
   Happy Birthday to you!
   Happy Birthday to you!
   Happy Birthday, dear Emily.
   Happy Birthday to you!

One function, but different results for different arguments.  Edit the call to
``happy_birthday("Andre")`` and run it again to see.

How it Works
------------

When Python sees ``happy_birthday("Emily")``, it:

1. Creates a local variable ``person`` inside the function.
2. Assigns it the value ``"Emily"``.
3. Executes the body of the function.
4. Discards ``person`` when the function finishes.

The next call ``happy_birthday("Andre")`` does the same thing with
``"Andre"``.

.. index:: parameter vs argument

Parameters vs. Arguments
--------------------------

The terms *parameter* and *argument* are often used interchangeably, but
technically:

- A *parameter* is the name listed in the ``def`` line: ``person``.
- An *argument* is the value supplied in the call: ``"Emily"``.
