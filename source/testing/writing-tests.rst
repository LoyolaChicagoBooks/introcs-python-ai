.. index:: testing; effective, pytest.raises, edge cases
   ACM-IEEE CS2013; SE6 Software Construction
   ACM-IEEE CS2023; SE6 Software Construction
   ACM-IEEE CS2013; SE7 Verification and Validation
   ACM-IEEE CS2023; SE7 Verification and Validation

.. _Writing-Tests:

Writing Effective Tests
=======================

Good tests are specific, independent, and cover edge cases.  Each test
function should check one thing and have a name that explains what
scenario it is testing.

Testing the Rational Class
---------------------------

.. index:: Rational; testing

Assuming ``Rational`` is defined in ``rational.py``:

.. literalinclude:: ../../examples/introcs-python/testing/test_rational.py
   :language: python
   :start-after: # start: basic_tests
   :end-before: # end: basic_tests

Testing for Exceptions
-----------------------

.. index:: pytest.raises

Use ``pytest.raises`` as a context manager to verify that an exception
is raised in the expected situation:

.. code-block:: python

   import pytest
   from rational import Rational

   def test_zero_denominator() -> None:
       with pytest.raises(ValueError):
           Rational(1, 0)

If the block inside ``with pytest.raises(ValueError):`` does *not* raise
``ValueError``, the test fails.

Edge Cases
----------

.. index:: testing; edge cases

Always test:

- **Zero**: ``factorial(0)``, ``Rational(0, 5)``
- **Negative inputs**: ``Rational(-1, 2)``, ``Rational(1, -2)``
- **Boundary values**: the smallest and largest valid inputs
- **Already-normalised values**: ``Rational(1, 2)`` should stay ``1/2``
- **Idempotent operations**: adding zero, multiplying by one

.. literalinclude:: ../../examples/introcs-python/testing/test_rational.py
   :language: python
   :start-after: # start: edge_case_tests
   :end-before: # end: edge_case_tests

.. index:: test organisation, test suite

Organising Tests in a Class
-----------------------------

.. index:: test class

For a large module, group related tests in a class prefixed with
``Test``:

.. literalinclude:: ../../examples/introcs-python/testing/test_rational.py
   :language: python
   :start-after: # start: test_classes
   :end-before: # end: test_classes

pytest discovers and runs these automatically with no extra configuration.

.. index:: testing; single responsibility

One Assert per Test (Guideline)
---------------------------------

.. index:: testing; one assert per test

When a test contains many assertions and fails, it can be hard to tell
*which* assertion caused the failure.  Prefer one logical check per test
function so failure messages are immediately actionable.

.. seealso::

   Example-based tests only check the inputs you think to write down.
   The :ref:`Testing for Correctness <Functional-Correctness>` section of
   the Functional Programming chapter introduces **property-based testing**,
   which states a property that must hold for *every* input and lets a
   library search for counterexamples.
