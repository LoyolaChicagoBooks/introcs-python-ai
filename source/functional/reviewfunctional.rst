.. index:: review questions; functional programming

.. _Review-Functional:

Chapter Review Questions
========================

#.  In your own words, what makes a function **pure**?

#.  Classify each of the following as pure or side-effecting:

    a.  ``len(items)``
    b.  ``print(items)``
    c.  ``items.append(x)``
    d.  ``sorted(items)``

#.  What is a **higher-order function**?  Give one example that *takes* a
    function and one that *returns* a function.

#.  Three built-in shapes of data processing.

    a.  What does ``map`` do?
    b.  What does ``filter`` do?
    c.  What does ``functools.reduce`` do?

#.  Rewrite ``[n * n for n in nums if n % 2 == 0]`` using ``map`` and
    ``filter``.  Which version do you find clearer, and why?

#.  Why does ``reduce`` take a *start* value, and what does that value have
    to do with empty sequences?

#.  What is a **closure**?  In ``make_multiplier`` from this chapter, what
    does the returned function "remember"?

#.  The counter built with ``nonlocal`` is convenient but no longer pure.
    Explain why, and what you give up.

#.  What does ``functools.partial(power, exponent=2)`` produce, and how is
    it different from calling ``power``?

#.  If ``h = compose(f, g)``, which of ``f`` and ``g`` runs first when you
    call ``h(x)``?

#.  Aliasing.

    .. code-block:: python

       a = [1, 2, 3]
       b = a
       b.append(4)

    a.  What is ``a`` afterward?
    b.  How would you append to ``b`` without changing ``a``?

#.  Describe the **functional core, imperative shell** pattern.  Why is the
    core easy to test and the shell hard?

#.  Why does a dynamically typed language like Python rely on testing more
    than a statically typed one does?

#.  Three layers of testing.

    a.  What is a doctest, and where does it live?
    b.  How does a property-based test differ from an example-based test?
    c.  Give one property (invariant, round-trip, or oracle) you could test
        for a function that sorts a list.

#.  Name the three equivalent models of computation discussed in the
    overview, and say which one functional programming descends from.
