.. index:: comparison operators, relational operators

More Conditional Expressions
=============================

We introduced the basic comparison operators in the previous section.
Here we look at a few more expressions that produce Boolean results.

.. index:: in operator, not in operator

Membership Testing
------------------

The ``in`` operator tests whether a value appears in a sequence (string,
list, tuple, etc.).  Press **Try it live** and change the operands:

.. try_examples::
   :height: 240px

   >>> "lo" in "hello"
   True
   >>> "xyz" in "hello"
   False
   >>> 3 in [1, 2, 3, 4]
   True

``not in`` is the negation.  Try it live:

.. try_examples::
   :height: 200px

   >>> "xyz" not in "hello"
   True

.. index:: is operator, is not operator, None; testing

Identity: ``is`` and ``is not``
--------------------------------

The ``is`` operator tests whether two names refer to the *same object*, not
just equal values.  Its most common use is testing for ``None``.  Try it live:

.. try_examples::
   :height: 240px

   >>> x = None
   >>> x is None
   True
   >>> x is not None
   False

Use ``is None`` rather than ``== None`` — it is more precise and Pythonic.

.. index:: string; comparison, lexicographic order, ASCII; ordering

Comparison with Strings
-----------------------

String comparison uses lexicographic (dictionary) order.  Try it live:

.. try_examples::
   :height: 240px

   >>> "apple" < "banana"
   True
   >>> "Z" < "a"    # uppercase letters come before lowercase in ASCII
   True
   >>> "cat" == "cat"
   True

.. index:: chained comparison

Chained Comparisons Revisited
------------------------------

Python's chained comparisons work with all comparison operators.  Try it live:

.. try_examples::
   :height: 240px

   >>> score = 85
   >>> 0 <= score <= 100
   True
   >>> 'a' <= 'c' <= 'z'
   True

Each expression below evaluates to ``True`` or ``False``.  Press **Try it
live**, then change the operands and operators to test your understanding:

.. try_examples::
   :height: 280px

   >>> "lo" in "hello"        # membership
   True
   >>> 3 in [1, 2, 3, 4]
   True
   >>> "apple" < "banana"     # lexicographic order
   True
   >>> "Z" < "a"              # uppercase sorts before lowercase
   True
   >>> score = 85
   >>> 0 <= score <= 100      # chained comparison
   True

Be cautious when mixing ``is`` in a chain — it is unusual and can be
confusing.  For numeric range checks, chaining is clear and idiomatic.
