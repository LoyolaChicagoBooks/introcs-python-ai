.. index:: sorting, list; sort, sorted()
   ACM-IEEE CS2013; AL3 Fundamental Data Structures and Algorithms
   ACM-IEEE CS2023; AL3 Fundamental Data Structures and Algorithms

.. _Sorting:

Sorting
=======

.. index:: Timsort, O(N log N), sorting algorithm

Understanding how sorting works is essential even if you always use the
built-in methods in practice.

Python's Built-in Sort
-----------------------

.. index:: list.sort(), sorted(), key=, reverse=

``list.sort()`` sorts *in place* (modifies the list, returns ``None``).
``sorted(iterable)`` returns a *new* sorted list without modifying the
original.  Try it live and watch ``sort`` modify the list in place:

.. try_examples::
   :height: 220px

   >>> nums = [3, 1, 4, 1, 5, 9, 2]
   >>> nums.sort()
   >>> print(nums)
   [1, 1, 2, 3, 4, 5, 9]

The ``key`` and ``reverse`` arguments control how ``sorted()`` orders
items.  Try it live: sort by ``len``, in reverse, or with your own ``key``:

.. try_examples::
   :height: 280px

   >>> words = ["banana", "apple", "cherry", "fig"]
   >>> print(sorted(words))               # alphabetical
   ['apple', 'banana', 'cherry', 'fig']
   >>> print(sorted(words, key=len))      # by length
   ['fig', 'apple', 'banana', 'cherry']
   >>> print(sorted(words, reverse=True)) # reverse alphabetical
   ['fig', 'cherry', 'banana', 'apple']

.. _Functions-as-Values:

Functions as Values
-------------------

.. index:: lambda, higher-order function, function; as value
   pure function, side effects, functional programming

Look again at ``sorted(words, key=len)``.  You did not call ``len`` —
you handed the function itself to ``sorted`` and let it do the calling.
In Python a function is a value like any other: you can store it in a
variable, pass it to another function, or return it.  A function that
takes another function as an argument (the way ``sorted`` takes ``key``)
is called a **higher-order function**.

When the function you want to pass is small, naming it with ``def`` is
more trouble than it is worth.  A **lambda** is a short, unnamed function
written inline.  You write the keyword ``lambda``, then its parameters, a
colon, and a single expression.  So ``lambda w: w[-1]`` reads as "given
``w``, give back ``w[-1]``, its last letter" — the same as a one-line
``def`` that returns ``w[-1]``, but with no name and no ``return``
keyword.  A lambda is a single expression, and its value is whatever that
expression produces.  Lambdas earn their place when there is no built-in
that does what you need:

.. try_examples::
   :height: 280px

   >>> words = ["banana", "apple", "cherry", "fig"]
   >>> print(sorted(words, key=lambda w: w[-1]))        # by last letter
   ['banana', 'apple', 'fig', 'cherry']
   >>> print(sorted(words, key=lambda w: (len(w), w)))  # length, then alphabetical
   ['fig', 'apple', 'banana', 'cherry']

The second key, ``lambda w: (len(w), w)``, returns a tuple, so the words
sort by length first and then alphabetically among ties.

Passing small functions around like this is your first taste of
*functional thinking*, and it pairs with a second idea you have already
met.  ``sorted`` returns a *new* list; ``list.sort`` changes the list in
place.  ``sorted`` is a **pure function**: it computes a result from its
arguments and does nothing else, so the same input always gives the same
output.  ``list.sort`` has a **side effect**: it modifies something and
returns ``None``.

.. try_examples::
   :height: 300px

   >>> nums = [3, 1, 2]
   >>> result = sorted(nums)    # pure: builds a new list
   >>> print(result, nums)      # original untouched
   [1, 2, 3] [3, 1, 2]
   >>> nums.sort()              # side effect: changes nums
   >>> print(nums)
   [1, 2, 3]

Neither style is wrong.  Pure functions are easier to test and reason
about, because you only have to think about what goes in and what comes
out.  Side effects are how a program changes the world — printing,
writing files, updating a list in place.  The skill is knowing which one
you are using.  We come back to functional thinking — ``map``,
``filter``, and writing your own higher-order functions — after
:ref:`Recursion <Recursion-Intro>`.

Selection Sort
--------------

.. index:: selection sort

Selection sort finds the minimum of the unsorted portion and swaps it
into place.  It always makes exactly N-1 swaps, but O(N²) comparisons:

.. literalinclude:: ../../examples/introcs-python/lists/sorting.py
   :language: python
   :start-after: # start: selection_sort
   :end-before: # end: selection_sort

.. code-block:: python

   nums = [12, 8, -5, 22, 9, 2]
   selection_sort(nums)
   print(nums)

Output:

.. code-block:: none

   [-5, 2, 8, 9, 12, 22]

Python's tuple-assignment swap ``a, b = b, a`` eliminates the need for
a temporary variable.

Bubble Sort
-----------

.. index:: bubble sort

Bubble sort repeatedly compares adjacent elements and swaps them if
they are out of order.  After each pass the largest unsorted element
"bubbles" to its correct position.  Both swaps and comparisons are
O(N²):

.. literalinclude:: ../../examples/introcs-python/lists/sorting.py
   :language: python
   :start-after: # start: bubble_sort
   :end-before: # end: bubble_sort

.. code-block:: python

   nums = [12, 8, -5, 22, 9, 2]
   bubble_sort(nums)
   print(nums)

Output:

.. code-block:: none

   [-5, 2, 8, 9, 12, 22]

Insertion Sort
--------------

.. index:: insertion sort

Insertion sort builds a sorted sublist from the left, inserting each
new element into its correct position.  It is efficient for nearly-sorted
data:

.. literalinclude:: ../../examples/introcs-python/lists/sorting.py
   :language: python
   :start-after: # start: insertion_sort
   :end-before: # end: insertion_sort

.. code-block:: python

   nums = [12, 8, -5, 22, 9, 2]
   insertion_sort(nums)
   print(nums)

Output:

.. code-block:: none

   [-5, 2, 8, 9, 12, 22]

.. index:: sorting; algorithm comparison, Big-O notation; sorting

Algorithm Comparison
--------------------

.. index:: sorting; performance

+-------------------+------------------+------------------+
| Algorithm         | Comparisons      | Swaps            |
+===================+==================+==================+
| Bubble sort       | O(N²)            | O(N²)            |
+-------------------+------------------+------------------+
| Selection sort    | O(N²)            | O(N)             |
+-------------------+------------------+------------------+
| Insertion sort    | O(N²) avg        | O(N²) avg        |
+-------------------+------------------+------------------+
| Python ``sort()`` | O(N log N)       | O(N log N)       |
+-------------------+------------------+------------------+

For any real application use ``list.sort()`` or ``sorted()``.  Study
the O(N²) algorithms to understand the problem; use the built-in to
solve it.
