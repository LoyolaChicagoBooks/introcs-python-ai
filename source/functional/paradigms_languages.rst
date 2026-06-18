.. index:: programming language; paradigm, type system, static typing
   dynamic typing, type safety, type error, strong typing
   ACM-IEEE CS2013; PL2 Functional Programming
   ACM-IEEE CS2023; PL2 Functional Programming

.. _Paradigms-and-Languages:

Paradigms, Languages, and Types
===============================

.. note::

   *Source:* Adapted from Läufer and Thiruvathukal,
   *Type-Safe Functional Programming for Computer Science and Data Science*
   (IEEE eScience 2025 workshop;
   `scalaworkshop.cs.luc.edu <https://scalaworkshop.cs.luc.edu>`_), recast
   from Scala into Python.

The functional style did not appear in a vacuum.  This section places it
among programming languages and their type systems, and ends with the
reason a dynamic language like Python depends so heavily on testing — the
idea the rest of the chapter builds on.

A Few Paradigm-Defining Languages
---------------------------------

A handful of languages introduced ideas that everything since has built
on.  The list below is deliberately short; the :ref:`Episodes in Computing
History <Computing-History>` chapter tells the fuller story.

- **FORTRAN** (1957) — imperative scientific computing.
- **LISP** (1958) — the first functional language, built on the lambda
  calculus, and for decades the language of artificial intelligence.
- **Simula** (1967) and **Smalltalk** (1972) — object-oriented programming.
- **Prolog** (1972) — logic programming.
- **ML** (1978) and its descendants (OCaml, Haskell, F#, Scala) —
  statically typed functional programming.
- **Python** (1991) — dynamic, multi-paradigm, and now dominant in data
  science and machine learning.

Two threads matter for us.  First, the functional idea is old: LISP put the
lambda calculus to work in the 1950s.  Second, AI has always tracked these
languages — symbolic AI ran on LISP and Prolog, while today's machine
learning runs on Python.  Python's appeal there is not raw speed but
expressiveness and a vast ecosystem, with the heavy numerical work handed
off to libraries written in C.

Type Systems
------------

A **type system** classifies the values a program computes — integers,
strings, lists — and checks that operations are used on the right kinds of
value.  Adding two numbers is fine; adding a number to a string is a **type
error**.  **Type safety** is the use of a type system to keep such errors
from happening.

Type systems vary along a few dimensions:

- **Static vs. dynamic** — are types checked before the program runs
  (static, as in Java or Rust) or while it runs (dynamic, as in Python)?
- **Strong vs. weak** — how firmly does the language refuse to mix
  incompatible types?
- **Inferred vs. explicit** — must you write the types out, or can the
  compiler work them out for you?

Python is **dynamically and strongly typed**: it will not silently add an
``int`` to a ``str`` (try it and you get a ``TypeError``), but it discovers
the problem only when that line actually runs.

The Static–Dynamic Pendulum
---------------------------

Languages have swung back and forth on this question:

- From the mid-1980s, **statically typed object-oriented** languages (C++,
  Java, C#) prized type safety and performance: the compiler catches whole
  categories of mistakes before the program ever runs.
- From the late 1990s, **dynamic** languages (Perl, Python, Ruby) traded
  some of that up-front checking for productivity — less ceremony, faster
  experimentation, an interactive REPL.  Without a compiler to lean on,
  these communities leaned on **automated testing** instead to build
  confidence that their code was correct.
- From the late 2000s, statically typed **functional** languages (Haskell,
  Scala, F#) tried to get the best of both: strong type safety with the
  expressiveness and immutability of the functional style.

Python sits firmly in the dynamic camp — and that has a direct
consequence for how you work.

Why This Leads to Testing
-------------------------

In a statically typed language, the compiler is a first line of defence:
many errors are caught before the program runs.  Python gives that up in
exchange for flexibility.  Nothing checks your program until you run it, so
the burden of showing that it is correct falls on **you**, through tests.

This is where the functional style pays off.  Pure functions — the ones
that just compute a result from their arguments — are the easiest things in
any program to test, because their behaviour depends on nothing but their
inputs.  A dynamic language *needs* rigorous testing, and a functional
design *makes* testing straightforward.  The two fit together, and the
:ref:`Testing for Correctness <Functional-Correctness>` section shows how
far you can take that pairing.
