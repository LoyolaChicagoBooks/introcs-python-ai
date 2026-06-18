.. index:: while statement, loop; while
   ACM-IEEE CS2013; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2023; SDF2 Fundamental Programming Concepts

.. _While-Statements:

While Statements
================


We have seen that programs can branch with ``if`` statements and call
functions.  The last essential control structure is *repetition* — executing
a block of code over and over.  The simplest loop in Python is the ``while``
loop.

If you heard someone say "While your tea is too hot, add a chip of ice,"
you would understand intuitively: test, act, test again, act again, and stop
when the condition is no longer true.  Python's syntax works the same way:

.. code-block:: none

   while condition:
       statement(s)

The condition is tested *before* each iteration.  If it is ``True``, the
body executes; then the condition is tested again.  When the condition
becomes ``False``, the loop exits and execution continues after the loop.

The Cooling Tea Example
-----------------------

Suppose tea starts at 115 °F and we want it at 112 °F; each chip of ice
lowers the temperature by one degree.  Run it, then try changing the
starting temperature or the target:

.. try_examples::
   :height: 280

   >>> temperature = 115
   >>> while temperature > 112:
   ...     print(f"Temperature: {temperature}°F — adding ice.")
   ...     temperature -= 1
   ...
   Temperature: 115°F — adding ice.
   Temperature: 114°F — adding ice.
   Temperature: 113°F — adding ice.
   >>> print(f"Tea is ready at {temperature}°F.")
   Tea is ready at 112°F.

.. index:: loop tracing, loop; trace table

Tracing a Loop
--------------

To understand a loop, trace through it by tracking the variable before
each test:

.. list-table::
   :header-rows: 1
   :widths: 20 30 20

   * - ``temperature``
     - condition ``> 112``
     - Action
   * - 115
     - True
     - body
   * - 114
     - True
     - body
   * - 113
     - True
     - body
   * - 112
     - False
     - exit

Countdown Example
-----------------

This loop counts down from 5, printing each value, then prints a final
message once the condition becomes false.  Run it, then change the starting
``count`` or the continuation condition and predict how many lines it prints:

.. try_examples::
   :height: 280

   >>> count = 5
   >>> while count > 0:
   ...     print(count)
   ...     count -= 1
   ...
   5
   4
   3
   2
   1
   >>> print("Blastoff!")
   Blastoff!

.. index:: infinite loop

Infinite Loops
--------------

If the condition never becomes ``False``, the loop runs forever.  This
is almost always a bug:

.. code-block:: python

   # BUG: count never changes
   count = 5
   while count > 0:
       print(count)   # loops forever

Press **Ctrl-C** to interrupt a runaway loop in the terminal.

.. index:: while True, break

``while True`` and ``break``
-----------------------------

Python has no ``do``-``while`` statement.  The idiomatic replacement is
``while True:`` with an explicit ``break`` to exit when done:

.. code-block:: python

   while True:
       answer = input("Type 'yes' to continue: ")
       if answer == "yes":
           break
       print("Please type 'yes'.")
   print("Continuing...")

``break`` immediately exits the innermost loop.

.. index:: continue statement

``continue``
------------

``continue`` skips the rest of the current iteration and jumps back to
test the condition.  Run it to see only the odd numbers printed:

.. try_examples::
   :height: 260

   >>> i = 0
   >>> while i < 10:
   ...     i += 1
   ...     if i % 2 == 0:
   ...         continue      # skip even numbers
   ...     print(i)          # prints 1 3 5 7 9
   ...
   1
   3
   5
   7
   9

.. index:: loop planning rubric, loop design

Loop Planning Rubric
--------------------

When designing a ``while`` loop, answer these questions:

1. **What changes each iteration?**  Identify the loop-driving variable(s).
2. **What is the initial value?**  Set it before the loop.
3. **What is the continuation condition?**  The loop runs *while* this is ``True``.
4. **How does the body update the variable?**  Ensure the condition
   eventually becomes ``False``.
5. **What happens after the loop?**  Handle any cleanup or output.
