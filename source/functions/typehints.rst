.. index:: type hints, type annotations, ->
   ACM-IEEE CS2013; PL4 Basic Type Systems
   ACM-IEEE CS2023; PL4 Basic Type Systems

.. _Type-Hints-Functions:

Type Hints for Functions
========================

Python is *dynamically typed* — you do not have to declare what type a
variable holds.  But you *can* add optional type labels, called *type
hints* or *type annotations*, to make your intent clear to readers and
tools.

Annotating Parameters and Return Types
---------------------------------------

.. index:: type hints; function signature

Place a colon and a type after each parameter name, and use ``->``
before the return type:

.. try_examples::
   :height: 200px

   >>> def add(a: int, b: int) -> int:
   ...     return a + b
   ...
   >>> add(3, 4)
   7

Compare with the unannotated version:

.. code-block:: python

   def add(a, b):
       return a + b

Both definitions work identically at runtime.  The annotations are
purely informational — Python does not enforce them.

Here is the ``weekly_wages`` function from the previous section,
annotated:

.. code-block:: python

   def weekly_wages(hours: float, rate: float) -> float:
       """Return total weekly wages including overtime pay above 40 hours."""
       if hours <= 40:
           return hours * rate
       else:
           overtime = hours - 40
           return 40 * rate + overtime * rate * 1.5

The annotation ``hours: float`` says "this parameter is intended to be
a float"; ``-> float`` says "this function is intended to return a
float".  A reader — or an editor — can see that at a glance without
reading the body.

Annotating ``str`` and ``None``
---------------------------------

.. index:: type hints; str, type hints; None

Use the type names you already know: ``str``, ``int``, ``float``,
``bool``.  Functions that return nothing are annotated ``-> None``:

.. code-block:: python

   def happy_birthday(person: str) -> None:
       print("Happy Birthday to you!")
       print("Happy Birthday to you!")
       print(f"Happy Birthday, dear {person}.")
       print("Happy Birthday to you!")

``-> None`` indicates the function returns no value.  You may omit
it when the absence of a return value is obvious, but including it
makes the signature complete.

Annotations Are Not Enforced at Runtime
-----------------------------------------

.. index:: type hints; not enforced

Python will not raise an error if you pass the wrong type:

.. try_examples::
   :height: 200px

   >>> def add(a: int, b: int) -> int:
   ...     return a + b
   ...
   >>> add("hello", "world")
   'helloworld'

The annotations say ``int``, but passing strings runs fine and returns
the concatenated string — the hints are not enforced.

This is intentional — annotations are a *communication tool*, not a
constraint.  If you want enforcement, a static type checker such as
``mypy`` will catch mismatches before the program runs:

.. code-block:: none

   $ mypy myscript.py
   myscript.py:10: error: Argument 1 to "add" has incompatible type "str"; expected "int"

We cover ``mypy`` and static type checking more fully in the
:ref:`Testing` chapter.

A Note on Style
----------------

.. index:: type hints; style

You do not need to annotate every function.  A reasonable habit is:

- Annotate any function you expect others to call (or that you will
  call from many places).
- Skip annotations for tiny, one-off helpers where the types are
  obvious from context.

As the code in this book grows more complex, you will see type hints
used consistently on functions that accept or return non-trivial types.
The full annotation system — including collection types such as
``list[int]`` and ``dict[str, float]``, and union types such as
``str | None`` — is introduced in the :ref:`Dataclasses` chapter after
object-oriented programming.
