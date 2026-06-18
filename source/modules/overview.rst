.. index:: modules, import, scope, LEGB, global, nonlocal, __name__, __main__
   ACM-IEEE CS2013; PL6 Language Translation and Execution
   ACM-IEEE CS2023; PL6 Language Translation and Execution

.. _Modules-And-Variable-Scope:

Modules and Variable Scope
==========================

.. note::
   *Source:* Contributed by PhD students in COMP 501 at Loyola University Chicago.

As programs grow larger, fitting everything into a single file quickly becomes
unmanageable. Python's solution is **modules**: separate ``.py`` files that
organize related functions, classes, and constants into logical units. Along with
modules comes a formal understanding of **scope** — the rules that determine where
a variable exists and where it can be accessed.

.. index:: modules; benefits, modular programming, reusability; modules, maintainability; modules

Why Modules Matter
------------------

A module is simply a Python file that contains code you want to reuse elsewhere.

.. code-block:: python

   # math_utils.py
   def add(a: int, b: int) -> int:
       return a + b

You can then import and use it in another file:

.. code-block:: python

   import math_utils
   print(math_utils.add(3, 4))

Output:

.. code-block:: none

   7

The benefits of modular programming are:

1. **Reusability** — write a function once, use it in many files.
2. **Maintainability** — when something breaks, you know exactly which file to open.
3. **Readability** — smaller files are easier to read and understand.
4. **Teamwork** — different developers can work on separate modules independently.
5. **Abstraction** — hide implementation details and expose only the interface
   (functions and classes) that others need.

.. index:: import; patterns, from … import, import as; alias, sys.path, ImportError

Importing Modules
-----------------

Python provides several import patterns:

.. list-table::
   :header-rows: 1

   * - Syntax
     - Example
   * - ``import module``
     - ``import math``
   * - ``from module import name``
     - ``from math import sqrt``
   * - ``import module as alias``
     - ``import numpy as np``
   * - ``from module import *``
     - (avoid this — it clutters the namespace)

When you run ``import something``, Python looks in:

1. The current directory.
2. The Python standard library.
3. Any directories listed in ``sys.path``.

If it cannot find the module you will get an ``ImportError``.

.. index:: __name__ variable, __main__; entry-point guard, module; run vs import

The ``__name__`` Variable
^^^^^^^^^^^^^^^^^^^^^^^^^^

Every Python file has a special variable called ``__name__``.

- When a file is *run directly*, ``__name__`` equals ``"__main__"``.
- When a file is *imported*, ``__name__`` equals the module's name.

.. code-block:: python

   # greetings.py
   def hello() -> None:
       print("Hello!")

   if __name__ == "__main__":
       hello()   # runs only when executed directly, not when imported

This pattern lets you write code that behaves differently depending on whether it
is the entry point or a library being imported.

.. index:: scope; definition, LEGB rule; scope lookup, local scope, enclosing scope, global scope, built-in scope

Understanding Scope
-------------------

**Scope** determines where a variable exists and where it can be accessed. Python
resolves variable names using the **LEGB rule**, searching in this order:

1. **Local (L)** — inside the current function.
2. **Enclosing (E)** — inside any enclosing (outer) functions.
3. **Global (G)** — at the top level of the module.
4. **Built-in (B)** — Python's built-in names such as ``len`` and ``print``.

Run this and watch which ``x`` wins:

.. try_examples::
   :height: 300px

   >>> x = 10          # global
   >>> def outer() -> None:
   ...     x = 20      # enclosing
   ...     def inner() -> None:
   ...         x = 30  # local
   ...         print(x)
   ...     inner()
   ...
   >>> outer()
   30

Python finds ``x = 30`` at the local level and stops searching.

.. index:: variable shadowing, scope; shadowing

Variable Shadowing
^^^^^^^^^^^^^^^^^^

If a variable in an inner scope shares a name with one in an outer scope, it
**shadows** the outer variable within that scope.

Try it live and confirm the global ``x`` is untouched:

.. try_examples::
   :height: 260px

   >>> x = 5
   >>> def demo() -> None:
   ...     x = 10
   ...     print(x)   # prints 10, not 5
   ...
   >>> demo()
   10
   >>> print(x)       # prints 5 — the global x is unchanged
   5

Use distinct variable names to avoid accidental shadowing.

.. index:: global statement; modules, nonlocal statement, UnboundLocalError; global

Global and Nonlocal Variables
------------------------------

Sometimes a function needs to modify a variable that lives outside its local scope.

.. index:: global statement; example

Global Variables
^^^^^^^^^^^^^^^^^

Declaring a variable ``global`` inside a function allows it to modify that variable in the enclosing module scope:

.. try_examples::
   :height: 260px

   >>> count = 0
   >>> def increment() -> None:
   ...     global count
   ...     count += 1
   ...
   >>> increment()
   >>> print(count)
   1

Without the ``global`` keyword, Python would treat ``count`` inside the function
as a new local variable — and the assignment would raise an ``UnboundLocalError``.

.. index:: nonlocal statement; example, closure; nonlocal

Nonlocal Variables
^^^^^^^^^^^^^^^^^^^

``nonlocal`` is used in nested functions to modify a variable from the *enclosing*
(not global) scope.

.. try_examples::
   :height: 300px

   >>> def outer() -> None:
   ...     x = 5
   ...     def inner() -> None:
   ...         nonlocal x
   ...         x += 1
   ...     inner()
   ...     print(x)
   ...
   >>> outer()
   6

As a general rule, prefer returning values from functions rather than modifying
external state — it makes code easier to reason about.

.. index:: variable lifetime, garbage collection; Python, local variable; lifetime, global variable; lifetime

Variable Lifetime
-----------------

Every variable has a **lifetime** — the period it exists in memory:

- **Local variables** — created when a function is called, destroyed when it
  returns.
- **Global/module variables** — live as long as the program runs.
- **Imported module variables** — remain cached in memory until the interpreter
  exits.

Python automatically frees memory for objects that are no longer referenced
(garbage collection), so you rarely manage memory manually. However, be aware that
mutating a shared list inside a function affects every module that holds a reference
to that list.

.. index:: package; __init__.py, multi-file project, __init__.py

Organizing Multi-File Projects
-------------------------------

In larger projects, data structures and utilities are typically split across multiple
files inside a **package** — a directory that contains an ``__init__.py`` file.

.. code-block:: none

   datastructures/
       __init__.py
       node.py
       linked_list.py
       stack.py
       utils.py

- ``node.py`` defines the ``Node`` class.
- ``linked_list.py`` imports ``Node`` and implements ``LinkedList``.
- ``stack.py`` reuses ``LinkedList`` internally.
- ``utils.py`` provides helper functions.

You import from the package like this:

.. code-block:: python

   from datastructures.linked_list import LinkedList

.. index:: circular import; problem and fix, ImportError; circular

Avoiding Circular Imports
^^^^^^^^^^^^^^^^^^^^^^^^^^

A **circular import** occurs when module A imports module B, and module B also
imports module A. Python cannot finish loading either file and raises an
``ImportError``. The fix is to move shared code into a third utility module, or to
place the import inside a function rather than at the top of the file.

.. index:: NameError; undefined variable, UnboundLocalError; assign before use, ImportError; module not found

Common Errors
-------------

.. list-table::
   :header-rows: 1

   * - Error
     - Meaning
   * - ``NameError``
     - Variable is not defined anywhere in scope.
   * - ``UnboundLocalError``
     - Variable is used before being assigned; add ``global`` or fix the logic.
   * - ``ImportError``
     - Python cannot find the module on its search path.

Exercises
---------

1. Create two files: ``math_utils.py`` with an ``add`` function, and ``main.py``
   that imports and uses it. Observe how the ``__name__ == "__main__"`` pattern
   works when you run each file directly vs. import it.
2. Write a function that has a local variable with the same name as a global
   variable. Demonstrate that modifying the local variable does not affect the
   global one.
3. Write a function that correctly uses ``global`` to increment a counter each time
   it is called. Then rewrite it without ``global`` by returning the new value
   instead. Which version is cleaner?
4. Describe a scenario where ``nonlocal`` is necessary. Write a small example that
   demonstrates it.
5. Design a package layout for a simple student gradebook system with at least
   three modules. Describe what each module would contain.
