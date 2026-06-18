.. index:: module, import

Library Modules
===============

Python's strength comes partly from its enormous standard library and
ecosystem of third-party packages.  A *module* is a ``.py`` file containing
functions and variables you can use in your own programs.

.. index:: import statement

Importing a Module
------------------

Use the ``import`` statement to make a module available:

.. code-block:: python

   import math

After importing, access the module's contents with dot notation.  Press
**Try it live** to run the import and a few ``math`` calls:

.. try_examples::
   :height: 280px

   >>> import math
   >>> math.sqrt(2)
   1.4142135623730951
   >>> math.pi
   3.141592653589793
   >>> math.floor(3.7)
   3
   >>> math.ceil(3.2)
   4

.. index:: math module

The ``math`` Module
-------------------

The ``math`` module provides mathematical functions beyond what is built in:

.. list-table::
   :header-rows: 1
   :widths: 25 45

   * - Function / Constant
     - Description
   * - ``math.sqrt(x)``
     - Square root of ``x``
   * - ``math.pi``
     - The constant π ≈ 3.14159…
   * - ``math.e``
     - The constant e ≈ 2.71828…
   * - ``math.floor(x)``
     - Largest integer ≤ ``x``
   * - ``math.ceil(x)``
     - Smallest integer ≥ ``x``
   * - ``math.log(x)``
     - Natural logarithm of ``x``
   * - ``math.log(x, base)``
     - Logarithm of ``x`` in the given base
   * - ``math.sin(x)``, ``math.cos(x)``, ``math.tan(x)``
     - Trigonometric functions (``x`` in radians)
   * - ``math.degrees(x)``
     - Convert radians to degrees
   * - ``math.radians(x)``
     - Convert degrees to radians
   * - ``math.factorial(n)``
     - n!

.. index:: random module

The ``random`` Module
---------------------

The ``random`` module generates pseudo-random numbers, which is useful for
games and simulations.  We call ``random.seed(0)`` first so the results below
are reproducible; remove that line to get different numbers each run.  Press
**Try it live**:

.. try_examples::
   :height: 280px

   >>> import random
   >>> random.seed(0)           # make the results reproducible
   >>> random.randint(1, 6)     # simulates a die roll
   4
   >>> random.random()          # float in [0.0, 1.0)
   0.7579544029403025
   >>> random.choice(["rock", "paper", "scissors"])
   'paper'

.. index:: from … import

Selective Import
----------------

To import just specific names from a module, avoiding the module prefix, use
``from math import sqrt, pi``.  You can also import everything with
``from math import *`` (generally discouraged in larger programs), or give a
module a shorter alias with ``import math as m``.  Press **Try it live**:

.. try_examples::
   :height: 240px

   >>> from math import sqrt, pi
   >>> print(sqrt(16), round(pi, 4))
   4.0 3.1416
   >>> import math as m
   >>> print(m.factorial(5))
   120

.. index:: import; alias, import as

.. index:: import; where Python looks

How Python Finds Modules
------------------------

When you write ``import math``, Python looks for a module named ``math.py``
in a list of directories called the *path*.  The standard library is always on
the path, so built-in modules like ``math`` and ``random`` are always
available.

When you create your own ``.py`` files, Python can import them if they are in
the same directory as your script.

.. index:: module; user-defined, pair: module; .py file

Writing Your Own Module
-----------------------

Any ``.py`` file can be used as a module.  If you save the following in
``geometry.py``:

.. code-block:: python

   import math

   def circle_area(radius: float) -> float:
       return math.pi * radius ** 2

   def circle_circumference(radius: float) -> float:
       return 2 * math.pi * radius

Then another file can use it:

.. code-block:: python

   import geometry
   print(geometry.circle_area(5))
