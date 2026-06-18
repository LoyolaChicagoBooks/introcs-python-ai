.. index:: list, list; syntax, list; indexing, list; slicing
   ACM-IEEE CS2013; SDF3 Fundamental Data Structures
   ACM-IEEE CS2023; SDF3 Fundamental Data Structures

.. _List-Syntax:

List Syntax
===========

A *list* is an ordered, mutable sequence of values.  It is the most
commonly used collection in Python.

Creating Lists
--------------

.. index:: list; literal, list; constructor

Use square brackets to write a list literal:

.. code-block:: python

   nums = [4, 7, -2, 5]
   words = ["up", "down", "over"]
   empty = []
   mixed = [1, "hello", 3.14]   # mixed types are allowed

``list()`` converts any iterable to a list.  Try it live and convert a
string of your own:

.. try_examples::
   :height: 220px

   >>> chars = list("abc")
   >>> print(chars)
   ['a', 'b', 'c']

Indexing and Length
--------------------

.. index:: list; index, list; len(), negative index

Elements are accessed by integer index starting at 0.  Try it live and
index into the list yourself:

.. try_examples::
   :height: 240px

   >>> nums = [4, 7, -2, 5]
   >>> print(nums[0])    # first element
   4
   >>> print(nums[3])    # last element
   5
   >>> print(len(nums))  # number of elements
   4

Negative indices count from the end: ``nums[-1]`` is the last element,
``nums[-2]`` is the second-to-last, and so on.

Mutation
--------

.. index:: list; mutable

Unlike strings, lists can be changed after creation.  Try it live and
assign to a different index:

.. try_examples::
   :height: 220px

   >>> nums = [4, 7, -2, 5]
   >>> nums[2] = 99
   >>> print(nums)
   [4, 7, 99, 5]

Slicing
-------

.. index:: list; slicing, slice

A *slice* extracts a sub-list.  The syntax is ``lst[start:stop]``, which
returns elements from index ``start`` up to (but not including) ``stop``.
Try it live and edit the slice bounds:

.. try_examples::
   :height: 280px

   >>> nums = [10, 20, 30, 40, 50]
   >>> print(nums[1:4])   # indices 1, 2, 3
   [20, 30, 40]
   >>> print(nums[:3])    # from the beginning through index 2
   [10, 20, 30]
   >>> print(nums[2:])    # from index 2 to the end
   [30, 40, 50]
   >>> print(nums[:])     # a copy of the whole list
   [10, 20, 30, 40, 50]

A slice always produces a new list; the original is unchanged.

.. index:: list; membership test

Membership Test
---------------

.. index:: in; list membership

The ``in`` operator tests whether a value is anywhere in the list.  Try it
live and test for values of your own:

.. try_examples::
   :height: 220px

   >>> words = ["up", "down", "over"]
   >>> print("down" in words)
   True
   >>> print("around" in words)
   False

Iterating Over a List
---------------------

.. index:: for; list iteration

Use a ``for`` loop to visit each element.  Try it live and edit the words:

.. try_examples::
   :height: 220px

   >>> for word in ["cat", "dog", "bird"]:
   ...     print(word.upper())
   ...
   CAT
   DOG
   BIRD

To iterate with an index, use ``enumerate()``.  Try it live:

.. try_examples::
   :height: 240px

   >>> scores = [88, 73, 95]
   >>> for i, score in enumerate(scores):
   ...     print(f"{i}: {score}")
   ...
   0: 88
   1: 73
   2: 95
