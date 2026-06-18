.. index:: labs; functional programming

.. _lab-functional:

Lab: Functional Programming
===========================

Goals for this lab:

- Use ``map``, ``filter``, and ``reduce`` to process data without explicit
  loops.
- Write and use a closure.
- Refactor a side-effecting program into a pure core and an imperative
  shell.
- Test the pure core with both doctest and a property-based test.

1. Transform and Filter
-----------------------

Given ``prices = [19.99, 5.0, 42.5, 8.75, 100.0]``:

a.  Use ``map`` to produce a new list with 8% sales tax added to each price.
b.  Use ``filter`` to keep only the prices above ``10.0``.
c.  Use ``functools.reduce`` to compute the total of all prices, then check
    your answer against the built-in ``sum``.

For each part, also write the list-comprehension equivalent and decide which
reads more clearly.

2. A Closure
------------

Write a function ``make_between(low, high)`` that returns a *predicate* — a
function of one argument that returns ``True`` when its argument is in the
range ``[low, high]``.  Then use it with ``filter``:

.. code-block:: python

   >>> in_range = make_between(10, 50)
   >>> list(filter(in_range, [5, 12, 40, 99, 50]))
   [12, 40, 50]

3. Pure Core, Imperative Shell
------------------------------

Here is a program that does everything at once — reading, computing, and
printing all tangled together:

.. code-block:: python

   def report(path):
       total = 0
       count = 0
       for line in open(path):
           total += float(line)
           count += 1
       print(f"average = {total / count}")

a.  Identify every side effect in ``report``.
b.  Refactor it into a **pure core** — one or more pure functions that do the
    computing — and a thin **imperative shell** that does only the file
    reading and printing.
c.  Add a docstring with a doctest to each pure function, and run
    ``python -m doctest`` on your file.

4. A Property-Based Test
------------------------

Install hypothesis (``pip install hypothesis``) and write a property-based
test for your ``average`` function from exercise 3:

a.  State the **invariant** that the average of a non-empty list of integers
    lies between its smallest and largest element, and test it with
    ``@given``.
b.  Run it with ``pytest``.  Then change ``average`` to divide by
    ``len(scores) + 1`` and run the test again — confirm that hypothesis
    finds a counterexample and reports the smallest one it can.

5. Challenge: Functional Newton
-------------------------------

Using the ``iterate`` and ``converged_value`` helpers from the
:ref:`Worked Examples <Functional-Numerical>` section, write a ``sqrt(c)``
function that finds the square root of ``c`` as a fixed point of the step
``x -> (x + c / x) / 2`` (the Babylonian method).  Test it with an *oracle*
property against ``math.sqrt``.
