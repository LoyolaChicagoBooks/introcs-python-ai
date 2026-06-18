.. index:: list; methods, list; built-in functions

.. _List-Methods:

List Methods
============

Python lists come with a rich set of methods for adding, removing,
searching, and reordering elements.

Adding Elements
---------------

.. index:: list.append(), list.insert(), list.extend()

- ``append(x)`` adds ``x`` to the end — the most common way to grow a list.
- ``insert(i, x)`` inserts ``x`` before index ``i``.
- ``extend(other)`` appends all elements of ``other`` to the list.

Try it live and add elements of your own:

.. try_examples::
   :height: 280px

   >>> words = ["up", "down"]
   >>> words.append("over")
   >>> print(words)
   ['up', 'down', 'over']
   >>> words.insert(1, "under")
   >>> print(words)
   ['up', 'under', 'down', 'over']
   >>> words.extend(["in", "out"])
   >>> print(words)
   ['up', 'under', 'down', 'over', 'in', 'out']

Removing Elements
-----------------

.. index:: list.remove(), list.pop(), del

- ``remove(x)`` deletes the *first* occurrence of ``x``; raises
  ``ValueError`` if not found.
- ``pop(i)`` removes and *returns* the element at index ``i`` (default:
  last element).
- ``del lst[i]`` removes the element at index ``i`` without returning it.

Try it live and watch how each call changes the list:

.. try_examples::
   :height: 240px

   >>> nums = [3, 1, 4, 1, 5]
   >>> nums.remove(1)     # removes the first 1
   >>> print(nums)
   [3, 4, 1, 5]
   >>> last = nums.pop()  # removes and returns 5
   >>> print(last, nums)
   5 [3, 4, 1]

Searching
---------

.. index:: list.index(), list.count()

- ``index(x)`` returns the index of the first occurrence of ``x``;
  raises ``ValueError`` if not found.
- ``count(x)`` returns how many times ``x`` appears.

Try it live and search for other values:

.. try_examples::
   :height: 220px

   >>> nums = [3, 1, 4, 1, 5]
   >>> print(nums.index(4))   # position of the first 4
   2
   >>> print(nums.count(1))   # how many 1s
   2

Sorting and Reversing
---------------------

.. index:: list.sort(), list.reverse()

- ``sort()`` sorts the list *in place* (ascending by default).
- ``reverse()`` reverses the list *in place*.

Try it live and see how ``sort`` and ``reverse`` change the list:

.. try_examples::
   :height: 240px

   >>> nums = [3, 1, 4, 1, 5, 9]
   >>> nums.sort()
   >>> print(nums)
   [1, 1, 3, 4, 5, 9]
   >>> nums.reverse()
   >>> print(nums)
   [9, 5, 4, 3, 1, 1]

List methods mutate the list in place.  Run this, then add your own
``append``, ``insert``, ``pop``, and ``sort`` calls to see the effect:

.. try_examples::
   :height: 300px

   >>> words = ["up", "down"]
   >>> words.append("over")
   >>> words.insert(1, "under")
   >>> words.extend(["in", "out"])
   >>> print(words)
   ['up', 'under', 'down', 'over', 'in', 'out']
   >>> nums = [3, 1, 4, 1, 5]
   >>> print("first index of 1:", nums.index(1))
   first index of 1: 1
   >>> print("count of 1:", nums.count(1))
   count of 1: 2
   >>> nums.sort()
   >>> print("sorted:", nums)
   sorted: [1, 1, 3, 4, 5]

Built-in Functions
------------------

.. index:: sorted(), min(), max(), sum(), reversed()

These built-in functions work on any iterable and do *not* modify the
original list:

- ``sorted(lst)`` returns a new sorted list.
- ``reversed(lst)`` returns an iterator over the list in reverse order.
- ``min(lst)``, ``max(lst)`` return the smallest and largest element.
- ``sum(lst)`` returns the sum of all elements (numbers only).

Try it live and confirm the original list is unchanged:

.. try_examples::
   :height: 220px

   >>> nums = [3, 1, 4, 1, 5]
   >>> print(sorted(nums))    # new list; nums unchanged
   [1, 1, 3, 4, 5]
   >>> print(min(nums), max(nums), sum(nums))
   1 5 14

.. index:: list; concatenation, list; repetition

Concatenation and Repetition
------------------------------

.. index:: list; +, list; *

The ``+`` operator concatenates two lists into a new one; ``*``
repeats a list.  Try it live and edit the operands:

.. try_examples::
   :height: 220px

   >>> a = [1, 2]
   >>> b = [3, 4]
   >>> print(a + b)
   [1, 2, 3, 4]
   >>> print(a * 3)
   [1, 2, 1, 2, 1, 2]

Note that ``+`` is different from ``extend``: ``+`` produces a *new*
list and leaves both operands unchanged, while ``extend`` mutates the
list it is called on.
