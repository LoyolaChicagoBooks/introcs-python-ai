.. index:: doctest, property-based testing, hypothesis, correctness
   testing; pure functions, example-based testing
   property-based testing; invariant, property-based testing; round-trip
   property-based testing; oracle
   ACM-IEEE CS2013; PL2 Functional Programming
   ACM-IEEE CS2013; SDF Software Development Fundamentals
   ACM-IEEE CS2023; PL2 Functional Programming
   ACM-IEEE CS2023; SE Software Engineering

.. _Functional-Correctness:

Testing for Correctness
=======================

This is where the chapter pays off.  A pure function is the easiest thing
in any program to test, because its result depends on nothing but its
arguments — no files, no clock, no hidden state, no setup.  Give it the same
inputs and it gives the same output, every time.  A dynamic language like
Python gives you no compiler to catch mistakes ahead of time
(:ref:`Paradigms, Languages, and Types <Paradigms-and-Languages>`), so the
job of showing your code is correct falls to tests — and a functional design
makes that job easy.  We build it up in three layers.

Layer 1: doctest
----------------

You have been reading tests since the start of this book.  Every **Try it
live** block is written in **doctest** format: a ``>>>`` line with its
expected output underneath.  doctest is a standard-library module that finds
those examples inside a function's docstring and checks that the output
still matches:

.. code-block:: python

   def average(scores):
       """Return the mean of a list of numbers.

       >>> average([92, 85, 79])
       85.33333333333333
       >>> average([])
       0.0
       """
       return sum(scores) / len(scores) if scores else 0.0

Run the file's doctests from the terminal:

.. code-block:: bash

   python -m doctest pure_core.py -v

doctests are documentation and tests at once: the docstring shows a reader
how to call the function, and ``doctest`` guarantees the example has not
gone stale.  They are perfect for the small, pure functions of a functional
core.

Layer 2: Example-Based Tests
----------------------------

For anything beyond a one-line example, write proper tests with ``pytest``,
as in the :ref:`Testing <Pytest-Intro>` chapter.  An **example-based** test
picks specific inputs and asserts the expected output:

.. code-block:: python

   from pure_core import average, letter_grade

   def test_average_simple():
       assert average([92, 85, 79]) == (92 + 85 + 79) / 3

   def test_letter_grade_boundaries():
       assert letter_grade(90) == "A"
       assert letter_grade(89.9) == "B"
       assert letter_grade(0) == "F"

Picking good examples — ordinary cases, boundaries, and the empty case — is
a skill the :ref:`Writing Effective Tests <Writing-Tests>` section covers in
depth.  But notice the limitation: you only ever test the inputs you thought
to write down.  The bug hiding at the input you *didn't* think of slips
through.

Layer 3: Property-Based Testing
-------------------------------

**Property-based testing** attacks that limitation.  Instead of naming
specific inputs, you state a **property** that must hold for *every* input,
and a library generates hundreds of cases — including awkward ones you would
never pick by hand — trying to find a counterexample.  The library here is
**hypothesis** (``pip install hypothesis``).

The ``@given`` decorator says what kind of inputs to generate.  A few
property shapes cover most situations.  An **invariant** is something that is
always true of the result — the mean of a list always lies between its
smallest and largest element:

.. literalinclude:: ../../examples/introcs-python/functional/test_properties.py
   :language: python
   :start-after: # start: invariant
   :end-before: # end: invariant

A **round-trip** property checks that one operation undoes another —
reversing a list twice gives back the original:

.. literalinclude:: ../../examples/introcs-python/functional/test_properties.py
   :language: python
   :start-after: # start: roundtrip
   :end-before: # end: roundtrip

An **oracle** property checks your function against a simpler, trusted one.
Newton's method on *x² − c* should agree with ``math.sqrt``:

.. literalinclude:: ../../examples/introcs-python/functional/test_properties.py
   :language: python
   :start-after: # start: oracle
   :end-before: # end: oracle

Run them with ``pytest`` like any other tests:

.. code-block:: bash

   python -m pytest test_properties.py

The binary search from the :ref:`Recursion <Recursion-Examples>` chapter is
a natural fit too — for *any* sorted list and *any* key, the result is
either ``-1`` or a valid index holding that key:

.. literalinclude:: ../../examples/introcs-python/recursion/binary_search_helper.py
   :language: python
   :start-after: # start: hypothesis_test
   :end-before: # end: hypothesis_test

Property tests are good at finding edge cases you would never write down by
hand.  Stated as the invariant above but over *floating-point* numbers, the
average property actually fails: hypothesis discovers that averaging several
identical large floats can land a whisker outside ``[min, max]``, because
floating-point division rounds.  That is not a flaw in your reasoning — it is
floating-point arithmetic showing its seams, surfaced by a test you barely
had to write.  This is the reward for a functional design: when your logic
lives in pure functions, you can hand it to a tool that tries thousands of
inputs and tells you the truth about your code.
