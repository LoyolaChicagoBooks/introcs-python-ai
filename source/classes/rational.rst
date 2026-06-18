.. index:: class; Rational, operator overloading, dunder methods

.. _Rational-Class:

The Rational Class
==================

A *rational number* is a ratio of two integers: 2/3, -5/4, 7.  We build
a ``Rational`` class that stores numerator and denominator in lowest
terms and supports arithmetic with natural Python operators.

Class Definition and Normalisation
------------------------------------

.. index:: Rational; __init__, gcd

.. literalinclude:: ../../examples/introcs-python/classes/rational.py
   :language: python
   :start-after: # start: init
   :end-before: # end: init

``math.gcd`` reduces the fraction to lowest terms.  We force the
denominator to always be positive so ``-3/5`` is stored as ``(-3, 5)``
rather than ``(3, -5)``.

String Representation
---------------------

.. index:: Rational; __str__, __repr__

.. literalinclude:: ../../examples/introcs-python/classes/rational.py
   :language: python
   :start-after: # start: str_repr
   :end-before: # end: str_repr

Arithmetic Operators
--------------------

.. index:: Rational; __add__, __mul__, __sub__, __truediv__

Python calls ``__add__`` when ``+`` is used between two ``Rational``
objects:

.. literalinclude:: ../../examples/introcs-python/classes/rational.py
   :language: python
   :start-after: # start: arithmetic
   :end-before: # end: arithmetic

Comparison Operators
--------------------

.. index:: Rational; __eq__, __lt__

.. literalinclude:: ../../examples/introcs-python/classes/rational.py
   :language: python
   :start-after: # start: comparison
   :end-before: # end: comparison

Conversion Methods
------------------

.. index:: Rational; float()

.. literalinclude:: ../../examples/introcs-python/classes/rational.py
   :language: python
   :start-after: # start: float
   :end-before: # end: float

Putting It Together
--------------------

Here we create two ``Rational`` values and exercise the arithmetic and
display methods.  This cell folds in the full class so you can run it and
edit the numbers:

.. try_examples::
   :height: 360px

   >>> import math
   >>> class Rational:
   ...     def __init__(self, numerator: int, denominator: int = 1):
   ...         if denominator == 0:
   ...             raise ValueError("Denominator cannot be zero")
   ...         g = math.gcd(abs(numerator), abs(denominator))
   ...         sign = -1 if denominator < 0 else 1
   ...         self._num = sign * numerator // g
   ...         self._denom = sign * denominator // g
   ...     def __str__(self) -> str:
   ...         if self._denom == 1:
   ...             return str(self._num)
   ...         return f"{self._num}/{self._denom}"
   ...     def __add__(self, other):
   ...         return Rational(self._num * other._denom + other._num * self._denom,
   ...                         self._denom * other._denom)
   ...     def __mul__(self, other):
   ...         return Rational(self._num * other._num, self._denom * other._denom)
   ...     def __eq__(self, other):
   ...         if not isinstance(other, Rational):
   ...             return NotImplemented
   ...         return self._num == other._num and self._denom == other._denom
   ...     def __lt__(self, other):
   ...         return self._num * other._denom < other._num * self._denom
   ...     def __float__(self) -> float:
   ...         return self._num / self._denom
   ...
   >>> f = Rational(6, -10)
   >>> h = Rational(1, 2)
   >>> print(f)              # -3/5  (normalised automatically)
   -3/5
   >>> print(f + h)          # -1/10
   -1/10
   >>> print(f * h)          # -3/10
   -3/10
   >>> print(h > f)          # True
   True
   >>> print(float(f))       # -0.6
   -0.6

Python dispatches ``f + h`` to ``f.__add__(h)`` and ``h > f`` to
``h.__gt__(f)`` (derived automatically from ``__lt__`` and ``__eq__``
when Python can't find ``__gt__`` directly).

.. index:: @classmethod, class method; factory method

Static Parse Method
-------------------

.. index:: Rational; classmethod, @classmethod

A class method for parsing a string acts on the class itself rather than an
instance:

.. literalinclude:: ../../examples/introcs-python/classes/rational.py
   :language: python
   :start-after: # start: parse
   :end-before: # end: parse

.. code-block:: python

   print(Rational.parse("-12/30"))   # -2/5
   print(Rational.parse("1.125"))    # 9/8
   print(Rational.parse("7"))        # 7
