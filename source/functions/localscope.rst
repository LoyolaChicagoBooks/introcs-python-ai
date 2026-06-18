.. index:: scope, local scope

Local Scope
===========

Variables created inside a function are *local* to that function — they exist
only while the function is running and are invisible outside it.

.. index:: local variable

Local Variables
---------------

Consider this function.  Press **Try it live** to run the definition and the
call:

.. try_examples::
   :height: 240px

   >>> def compute_area(length: float, width: float) -> float:
   ...     area = length * width    # 'area' is a local variable
   ...     return area
   ...
   >>> compute_area(5, 3)
   15

The variables ``length``, ``width``, and ``area`` are all local.  After the
function returns, they are gone.  Trying to access ``area`` from outside the
function raises ``NameError: name 'area' is not defined``.

.. index:: scope; why local scope matters

Why Local Scope?
----------------

Local scope is a feature, not a limitation.  It means:

- Functions are *self-contained*.  A function cannot accidentally modify
  variables in other parts of the program.
- You can use the same name in different functions without conflict.

.. try_examples::
   :height: 280px

   >>> def add(a: int, b: int) -> int:
   ...     result = a + b    # this 'result' is local to add()
   ...     return result
   ...
   >>> def multiply(a: int, b: int) -> int:
   ...     result = a * b    # this 'result' is local to multiply()
   ...     return result
   ...
   >>> add(3, 4)
   7

Both functions have a variable named ``result``, but they are completely
independent.

.. index:: LEGB rule, scope; lookup order, enclosing scope, global scope, built-in scope

How Python Looks Up Names
--------------------------

When Python looks up a variable name inside a function, it searches in this
order (LEGB):

1. **Local** — variables assigned in the current function.
2. **Enclosing** — local variables of any enclosing functions (for nested
   functions, covered later).
3. **Global** — variables assigned at the top level of the module.
4. **Built-in** — names built into Python (``print``, ``len``, ``range``,
   etc.).

.. code-block:: python

   x = 10           # global

   def show() -> None:
       x = 99       # local — shadows the global
       print(x)

   show()           # prints 99
   print(x)         # prints 10 — global unchanged

.. index:: global statement

Using Global Variables (Avoid When Possible)
---------------------------------------------

If you *assign* to a name inside a function, Python treats it as local.  If
you want to modify a global variable, use the ``global`` statement:

.. code-block:: python

   count = 0

   def increment() -> None:
       global count
       count += 1

   increment()
   increment()
   print(count)    # 2

However, relying on global mutable state makes programs harder to understand
and test.  Prefer passing values as arguments and returning results.

Bad Scope Example
-----------------

Here is a common mistake:

.. code-block:: python

   def compute():
       total = a + b    # ERROR if a and b aren't defined somewhere above

If ``a`` and ``b`` are not local or global, Python raises a ``NameError``.
The fix is to pass them as parameters:

.. code-block:: python

   def compute(a: int, b: int) -> int:
       total = a + b
       return total
