.. index:: class; examples, Averager class, __repr__

.. _Class-Examples:

Class Instance Examples
=======================

The Averager Class
------------------

.. index:: Averager class

An ``Averager`` accumulates numeric values one at a time and reports
their running average.  It illustrates a class whose instance variables
track *changing internal state* rather than simply storing data:

.. literalinclude:: ../../examples/introcs-python/classes/averager.py
   :language: python
   :start-after: # start: Averager
   :end-before: # end: Averager

Run this self-contained version — feed it your own list of values and watch
the running average change:

.. try_examples::
   :height: 360px

   >>> class Averager:
   ...     def __init__(self):
   ...         self._count = 0
   ...         self._total = 0.0
   ...     def add_datum(self, value: float) -> None:
   ...         self._total += value
   ...         self._count += 1
   ...     def get_average(self) -> float:
   ...         if self._count == 0:
   ...             return float("nan")
   ...         return self._total / self._count
   ...     def get_count(self) -> int:
   ...         return self._count
   ...     def __str__(self) -> str:
   ...         return f"Averager({self._count} values, avg={self.get_average():.4f})"
   ...
   >>> avg = Averager()
   >>> for value in [3.0, 7.5, 2.0, 6.5]:
   ...     avg.add_datum(value)
   ...
   >>> print(avg.get_count(), "values")
   4 values
   >>> print(f"Average: {avg.get_average():.2f}")
   Average: 4.75
   >>> print(avg)
   Averager(4 values, avg=4.7500)

The ``_count`` and ``_total`` prefixes with ``_`` signal that these are
internal attributes not meant to be accessed from outside the class.

.. index:: dunder methods; __str__ vs __repr__, string representation

``__str__`` and ``__repr__``
-----------------------------

.. index:: __repr__

Python uses two methods for string representations:

- ``__str__`` is called by ``print()`` and ``str()`` — intended for
  human-readable output.
- ``__repr__`` is called in the interactive interpreter and by ``repr()``
  — intended for an unambiguous, developer-readable representation.

A useful rule: if possible, write ``__repr__`` so that ``eval(repr(obj))``
recreates the object.

Here we define ``Point`` and call both conversion functions to observe the
difference — run it and compare the two lines:

.. try_examples::
   :height: 340px

   >>> class Point:
   ...     def __init__(self, x: float, y: float):
   ...         self.x = x
   ...         self.y = y
   ...     def __str__(self) -> str:
   ...         return f"({self.x}, {self.y})"
   ...     def __repr__(self) -> str:
   ...         return f"Point({self.x!r}, {self.y!r})"
   ...
   >>> p = Point(3, 7)
   >>> print(str(p))    # uses __str__
   (3, 7)
   >>> print(repr(p))   # uses __repr__
   Point(3, 7)

A Distance Method
-----------------

.. index:: class; method with same-type parameter

Methods can accept parameters of the same class.  Here ``distance_to``
receives another ``Point``:

.. code-block:: python

       def distance_to(self, other: "Point") -> float:
           import math
           return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

Run this complete version and try other coordinates:

.. try_examples::
   :height: 300px

   >>> import math
   >>> class Point:
   ...     def __init__(self, x: float, y: float):
   ...         self.x = x
   ...         self.y = y
   ...     def distance_to(self, other: "Point") -> float:
   ...         return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
   ...
   >>> p1 = Point(0, 0)
   >>> p2 = Point(3, 4)
   >>> print(p1.distance_to(p2))
   5.0

Inside ``distance_to``, ``self`` refers to the object the method was
called on (``p1``), and ``other`` refers to the argument (``p2``).
Both are ``Point`` objects, and both sets of instance variables are
accessible.
