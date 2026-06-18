.. index:: immutability, pure function, side effects, aliasing
   functional core imperative shell
   ACM-IEEE CS2013; PL2 Functional Programming
   ACM-IEEE CS2023; PL2 Functional Programming

.. _Pure-Cores:

Immutable Data and Pure Cores
=============================

The functional style rests on two habits: writing pure functions, and
working with values that do not change.  The two reinforce each other, and
together they lead to a way of organising whole programs that keeps the
testable logic separate from the messy edges.

Why Immutability Helps
----------------------

Mutable data shared between two names is a classic source of bugs.  Because
assignment copies a *reference*, not the data, two variables can end up
pointing at the same list — and a change through one is visible through the
other:

.. try_examples::
   :height: 280px

   >>> a = [1, 2, 3]
   >>> b = a          # b and a refer to the same list
   >>> b.append(4)
   >>> a
   [1, 2, 3, 4]

This **aliasing** surprised you in the :ref:`Lists <Functions-as-Values>`
material, and it scales into hard-to-trace bugs once a list is passed
through several functions, any of which might mutate it.  The functional
remedy is to build a *new* value instead of changing an existing one:

.. try_examples::
   :height: 280px

   >>> a = [1, 2, 3]
   >>> b = a + [4]    # a fresh list; a is untouched
   >>> a
   [1, 2, 3]
   >>> b
   [1, 2, 3, 4]

Python also offers genuinely immutable types, which make accidental change
*impossible* rather than merely discouraged: tuples
(:ref:`Tuple Syntax <Tuple-Syntax>`), strings, and frozen dataclasses
(``@dataclass(frozen=True)``, from :ref:`Dataclasses`).  When a value
should never change after it is created, reaching for one of these turns a
whole class of bug into an error you find immediately.

Functional Core, Imperative Shell
---------------------------------

A program cannot be all pure functions — somewhere it must read input and
print results.  The useful pattern is to split the two cleanly:

- a **functional core** of pure functions that hold all the logic, and
- a thin **imperative shell** that does the input and output and nothing
  else.

Consider a small program that reads exam scores from a file and prints a
letter grade.  The logic divides into three pure functions — parse the
text, average the numbers, map the average to a letter — none of which
touches a file or the screen:

.. literalinclude:: ../../examples/introcs-python/functional/pure_core.py
   :language: python
   :start-after: # start: pure_core
   :end-before: # end: pure_core

Each of these is trivial to exercise on its own, because it depends only on
what you pass in:

.. try_examples::
   :height: 320px

   >>> def average(scores):
   ...     return sum(scores) / len(scores) if scores else 0.0
   ...
   >>> def letter_grade(avg):
   ...     for cutoff, letter in [(90, "A"), (80, "B"), (70, "C"), (60, "D")]:
   ...         if avg >= cutoff:
   ...             return letter
   ...     return "F"
   ...
   >>> average([92, 85, 79])
   85.33333333333333
   >>> letter_grade(average([92, 85, 79]))
   'B'

All the side effects live in one small shell function that reads the file,
calls the pure core, and prints — and makes no decisions of its own:

.. literalinclude:: ../../examples/introcs-python/functional/pure_core.py
   :language: python
   :start-after: # start: shell
   :end-before: # end: shell

The payoff is testing.  The shell is hard to test — it touches the file
system and the screen — but there is almost nothing in it to get wrong.
The core, where all the real logic lives, is pure, so you can test it
exhaustively without files, screens, or mocks.  The next two sections put
that to work.
