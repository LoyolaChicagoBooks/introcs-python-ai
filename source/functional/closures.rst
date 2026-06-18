.. index:: closure, functools.partial, function composition, nonlocal
   ACM-IEEE CS2013; PL2 Functional Programming
   ACM-IEEE CS2023; PL2 Functional Programming

.. _Closures:

Closures and Composition
========================

A higher-order function can *return* a function as well as take one.  When
it does, the returned function often needs to remember something from the
moment it was created.  A function bundled together with the variables it
remembers from its enclosing scope is called a **closure**.

Functions That Build Functions
------------------------------

``make_multiplier`` below takes a number and returns a *new function* that
multiplies by it.  The inner ``multiply`` uses ``factor``, which belongs to
the enclosing call — and it keeps working even after ``make_multiplier``
has returned, because the closure holds on to that value:

.. try_examples::
   :height: 320px

   >>> def make_multiplier(factor):
   ...     def multiply(x):
   ...         return x * factor
   ...     return multiply
   ...
   >>> triple = make_multiplier(3)
   >>> double = make_multiplier(2)
   >>> triple(10)
   30
   >>> double(10)
   20

``triple`` and ``double`` are two different closures built from the same
code, each remembering its own ``factor``.  You have already used a closure
without naming it: the ``helper`` inside ``binary_search`` in the
:ref:`Recursion <Recursion-Examples>` chapter closes over ``arr`` and
``key`` so it does not have to pass them through every recursive call.

A closure can also remember something that *changes*.  ``make_counter``
returns a function that hands back 1, 2, 3, … on successive calls; the
``nonlocal`` keyword lets the inner function update the ``count`` in the
enclosing scope:

.. try_examples::
   :height: 320px

   >>> def make_counter():
   ...     count = 0
   ...     def next_value():
   ...         nonlocal count
   ...         count += 1
   ...         return count
   ...     return next_value
   ...
   >>> c = make_counter()
   >>> c()
   1
   >>> c()
   2
   >>> c()
   3

Notice the trade-off: this counter is convenient, but it is *no longer a
pure function*.  Calling ``c()`` twice with no arguments gives two different
answers, because it carries hidden state.  Closures let you choose — keep
them pure when you can, and reach for mutable state only when the problem
genuinely needs memory.

Fixing Some Arguments: ``partial``
----------------------------------

A common reason to build a function from another is to *fix* some of its
arguments.  ``functools.partial`` does exactly that: give it a function and
some arguments, and it returns a new function that supplies them for you.

.. try_examples::
   :height: 320px

   >>> from functools import partial
   >>> def power(base, exponent):
   ...     return base ** exponent
   ...
   >>> square = partial(power, exponent=2)
   >>> cube = partial(power, exponent=3)
   >>> square(9)
   81
   >>> cube(2)
   8

``square`` is ``power`` with ``exponent`` nailed down to ``2``.  This is a
tidy alternative to writing ``lambda x: power(x, 2)`` and works well as a
``key`` or as an argument to ``map``.

Composing Functions
-------------------

If ``map``, ``filter``, and ``reduce`` are about applying functions to data,
**composition** is about combining functions with each other.  Mathematics
writes the composition of *f* and *g* as *f ∘ g*, meaning "apply *g*, then
apply *f*."  We can build a ``compose`` helper that does this for any number
of functions, right to left, using ``reduce``:

.. literalinclude:: ../../examples/introcs-python/functional/higher_order.py
   :language: python
   :start-after: # start: compose
   :end-before: # end: compose

.. try_examples::
   :height: 320px

   >>> from functools import reduce
   >>> def compose(*funcs):
   ...     return reduce(lambda f, g: lambda x: f(g(x)), funcs, lambda x: x)
   ...
   >>> double_then_increment = compose(lambda x: x + 1, lambda x: x * 2)
   >>> double_then_increment(10)
   21

The result of ``double_then_increment(10)`` is ``21``: the rightmost
function runs first (``10 * 2`` is ``20``), then the next (``20 + 1`` is
``21``).  Composition lets you assemble a complex transformation out of
small, individually testable steps — which is exactly the property the next
two sections depend on.
