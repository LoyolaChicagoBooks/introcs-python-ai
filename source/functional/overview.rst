.. index:: functional programming, paradigm, lambda calculus, pure function
   side effects, immutability, Church-Turing thesis, stored-program model
   Turing machine, von Neumann architecture, functional core imperative shell
   ACM-IEEE CS2013; PL2 Functional Programming
   ACM-IEEE CS2023; PL2 Functional Programming

.. _Functional-Programming:

Functional Programming
======================

.. note::

   *Source:* Adapted from Konstantin Läufer and George K. Thiruvathukal,
   *Type-Safe Functional Programming for Computer Science and Data Science*
   (IEEE eScience 2025 workshop, Chicago;
   `scalaworkshop.cs.luc.edu <https://scalaworkshop.cs.luc.edu>`_), recast
   from Scala into Python.

Mathematics has always been built on functions.  A function takes inputs
and produces an output, and the same inputs always produce the same
output.  ``sin``, ``log``, and "the area of a circle of radius *r*" are
all functions in this sense: they compute a value and do nothing else.
Programming inherited the word, but not always the idea.  In most code a
"function" also reads files, prints to the screen, or changes a variable
somewhere — it *does things* as well as *computes things*.

**Functional programming** is the style that takes the mathematical
meaning seriously: build programs out of functions that compute results
from their arguments, prefer values that do not change, and keep the
parts that *do things* small and separate.  You have already met the
core ideas in passing — :ref:`Functions as Values <Functions-as-Values>`
introduced higher-order functions and the difference between a pure
function and one with a side effect.  This chapter pulls those threads
together and shows why the style matters, especially when you care about
**correctness**.

A Family of Paradigms
---------------------

Functional programming is one of several **paradigms** — broad styles for
organising a program:

- **Imperative:** explicit, step-by-step changes to mutable state.
- **Functional:** results computed by pure, often recursive functions over
  immutable values.
- **Object-oriented:** public behaviour wrapped around private state.
- **Actors:** concurrent objects that communicate by messages.
- **Logic:** queries answered from a database of facts and rules.

Python is **multi-paradigm**: it supports all of these to some degree, and
real programs mix them.  The point of learning the functional style is not
to use it for everything, but to add it to the set of tools you reach for
when it fits.  (For the historical sweep of how these paradigms and their
languages arose, see :ref:`Episodes in Computing History
<Computing-History>`.)

Why Is So Much Code Imperative?
-------------------------------

If the mathematical ideal is a pure function, why does so much everyday
code look like a sequence of commands that change variables?  The answer
is that our machines are built that way.  The **stored-program model** —
the design behind nearly every computer, traced to Turing's abstract
machine (1936) and von Neumann's EDVAC report (1945) — describes a
processor that steps through instructions, reading and writing a large
shared memory.

That model has three moving parts: arithmetic on values, *sequencing* of
operations under some control, and a *memory* that the program keeps
changing.  Imperative programming mirrors the hardware almost directly: a
variable is a memory cell, assignment is a write, and a loop is the
control stepping along.  The style feels natural because it describes what
the machine literally does.

Three Models of Computation
---------------------------

The stored-program machine is not the only way to describe computation.
There are three classic models, and they are *equivalent in power* — each
can compute anything the others can:

- **The Turing machine / von Neumann architecture** — a model of the
  *hardware*: tape or memory, a read/write head, and a table of
  instructions.  Powerful, but low-level and a little unnatural as a way
  to *think*.
- **The lambda calculus** — a model of *computation itself*, invented by
  Alonzo Church in the 1930s.  It has almost nothing in it: variables,
  function definition, and function application.  It is simple,
  mathematical, and close to how we reason about functions.
- **Recursion** — a direct expression of the underlying mathematics, which
  you met in the :ref:`Recursion <Recursion-Intro>` chapter.

The **Church–Turing thesis** states that these models all capture exactly
the same notion of "what can be computed."  Functional programming descends
from the lambda calculus, which is why its building block — the anonymous
function, or ``lambda`` — carries that name.  The whole calculus fits in a
few lines of grammar:

.. code-block:: none

   <expr> ::= <name>                 # a variable
            | lambda <name>. <expr>  # a function of one argument
            | <expr> <expr>          # applying one expression to another

Everything else — numbers, booleans, data structures, loops — can be built
from just those three forms.  You do not need the details to use Python,
but it is worth knowing that the functional style rests on a foundation as
old and as solid as the machine model, and arguably closer to the way
mathematics already describes the world.

The Practical Tension
---------------------

Here is the catch.  A program that only computes values and never *does*
anything is useless: at some point it must read input, show a result, save
a file, or talk to the network.  Those are side effects, and you cannot
write a real program without them.  Pure functions alone are not enough.

The functional answer is not to ban side effects but to **contain** them.
Keep the logic of your program — the calculations, the decisions, the data
transformations — in pure functions that are easy to reason about and easy
to test.  Push the side effects out to a thin layer at the edges that does
the reading and printing and little else.  This arrangement has a name,
**functional core, imperative shell**, and the :ref:`Immutable Data and
Pure Cores <Pure-Cores>` section shows how to build it.

Why bother?  Because pure functions are *correct or not* in a way you can
check.  Given the same inputs they always behave the same way, so you can
pin their behaviour down with tests.  That is the throughline of this
chapter: the functional style is not abstraction for its own sake — it is
how you earn confidence that your program is right.

Road Map
--------

The rest of the chapter builds up the toolkit and then cashes it in for
correctness:

- :ref:`Paradigms, Languages, and Types <Paradigms-and-Languages>` — where
  the functional style sits among languages, and why a dynamic language
  like Python leans so heavily on testing.
- :ref:`Higher-Order Functions <Higher-Order-Functions>` — ``map``,
  ``filter``, and ``reduce``.
- :ref:`Closures and Composition <Closures>` — functions that capture and
  build other functions.
- :ref:`Immutable Data and Pure Cores <Pure-Cores>` — designing for a pure
  core and an imperative shell.
- :ref:`Worked Examples <Functional-Numerical>` — Newton's method and Monte
  Carlo π, in functional style.
- :ref:`Testing for Correctness <Functional-Correctness>` — doctest and
  property-based testing, the payoff for keeping functions pure.
