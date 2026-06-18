.. index:: searching, linear search, binary search
   ACM-IEEE CS2013; AL3 Fundamental Data Structures and Algorithms
   ACM-IEEE CS2023; AL3 Fundamental Data Structures and Algorithms

.. _Searching:

Searching
=========

Searching finds whether a value exists in a collection and, if so,
where.  Python provides both built-in conveniences and the ability to
write searches explicitly.

Linear Search
-------------

.. index:: linear search, in; search

A *linear search* examines each element one by one until it finds the
target or exhausts the list.  It works on any list, sorted or not.

**Using the ``in`` operator** (membership only) and **``list.index()``**
(returns the position).  Try it live and search for values of your own:

.. try_examples::
   :height: 240px

   >>> data = [12, 8, -5, 22, 9, 2]
   >>> print(7 in data)
   False
   >>> print(9 in data)
   True
   >>> print(data.index(9))
   4

``index()`` raises ``ValueError`` if the value is not in the list.
To avoid the exception, check with ``in`` first.  Try it live:

.. try_examples::
   :height: 240px

   >>> data = [12, 8, -5, 22, 9, 2]
   >>> target = 22
   >>> if target in data:
   ...     print(f"Found at index {data.index(target)}")
   ... else:
   ...     print("Not found")
   ...
   Found at index 3

Writing Linear Search Explicitly
---------------------------------

.. index:: linear search; explicit

Writing the search as a loop is useful when you need more control —
for example, to return the *index* on the first match, or to search
through a list of objects by a field:

Try it live and search for different targets:

.. try_examples::
   :height: 300px

   >>> def linear_search(data: list, target) -> int:
   ...     for i, value in enumerate(data):
   ...         if value == target:
   ...             return i
   ...     return -1    # not found
   ...
   >>> data = [12, 8, -5, 22, 9, 2]
   >>> print(linear_search(data, 9))
   4
   >>> print(linear_search(data, 99))
   -1

Continuing a Search
^^^^^^^^^^^^^^^^^^^^

To find all occurrences, collect every matching index:

Try it live and find every matching index:

.. try_examples::
   :height: 240px

   >>> def find_all(data: list, target) -> list[int]:
   ...     return [i for i, v in enumerate(data) if v == target]
   ...
   >>> print(find_all([1, 3, 1, 4, 1], 1))
   [0, 2, 4]

Binary Search
-------------

.. index:: binary search, bisect module

Linear search examines up to N elements — slow for large sorted lists.
*Binary search* repeatedly halves the search space, requiring only
O(log N) comparisons — but the list must be sorted.

Python's ``bisect`` module provides binary search.  Try it live and search
the sorted list for other values:

.. try_examples::
   :height: 300px

   >>> import bisect
   >>> data = [-5, 2, 8, 9, 12, 22]   # must be sorted
   >>> i = bisect.bisect_left(data, 9)
   >>> if i < len(data) and data[i] == 9:
   ...     print(f"Found at index {i}")
   ... else:
   ...     print("Not found")
   ...
   Found at index 3

``bisect_left(data, target)`` returns the leftmost position where
``target`` could be inserted to keep ``data`` sorted.  If
``data[i] == target``, the value is present.

.. index:: Big-O notation, O(N) vs O(log N)

Performance Comparison
-----------------------

+-------------------+-----------+----------------------------+
| Search type       | Time      | Requirement                |
+===================+===========+============================+
| ``in`` / linear   | O(N)      | Any list                   |
+-------------------+-----------+----------------------------+
| ``bisect``        | O(log N)  | List must be sorted        |
+-------------------+-----------+----------------------------+

For small lists the difference is negligible.  For large sorted lists,
binary search is dramatically faster.
