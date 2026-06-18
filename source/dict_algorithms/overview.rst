.. index:: dictionary algorithms, counting, grouping, filtering, merging, frequency
   ACM-IEEE CS2013; SDF3 Fundamental Data Structures
   ACM-IEEE CS2023; SDF3 Fundamental Data Structures

.. _Dictionary-Algorithms:

Dictionary Algorithms
=====================

.. note::
   *Source:* Contributed by PhD students in COMP 501 at Loyola University Chicago.

Dictionaries are one of Python's most powerful data structures because they map keys
to values with extremely fast lookup times. As programs grow in size and complexity,
certain dictionary patterns appear again and again. This chapter covers the most
important ones.

.. index:: dict; counting pattern, frequency count, dict.get(); default zero

Counting with Dictionaries
--------------------------

Counting occurrences is one of the most common uses of a dictionary.

.. literalinclude:: ../../examples/introcs-python/dict_algorithms/patterns.py
   :language: python
   :start-after: # start: counting
   :end-before: # end: counting

Output:

.. code-block:: none

   {'apple': 3, 'banana': 2, 'pear': 1}

The ``.get()`` method makes this more concise:

.. code-block:: python

   counts = {}
   for w in words:
       counts[w] = counts.get(w, 0) + 1

``get(key, 0)`` returns the current count if the key exists, or ``0`` if it does
not, avoiding a ``KeyError``.

Run the counting pattern below, then change ``words`` — try counting the
characters in a string such as ``"mississippi"`` instead:

.. try_examples::
   :height: 240px

   >>> words = ["apple", "banana", "apple", "pear", "banana", "apple"]
   >>> counts = {}
   >>> for w in words:
   ...     counts[w] = counts.get(w, 0) + 1
   ...
   >>> print(counts)
   {'apple': 3, 'banana': 2, 'pear': 1}

.. index:: dict; filtering pattern, dict comprehension; filtering

Filtering Dictionaries
-----------------------

Build a new dictionary containing only the key/value pairs that satisfy a condition:

.. literalinclude:: ../../examples/introcs-python/dict_algorithms/patterns.py
   :language: python
   :start-after: # start: filtering
   :end-before: # end: filtering

Output:

.. code-block:: none

   {'Alice': 95, 'Bob': 82, 'Diana': 99}

.. index:: dict; grouping pattern, dict.setdefault(); grouping pattern

Grouping with Dictionaries
---------------------------

Grouping places items that share a characteristic into lists under a common key.

.. literalinclude:: ../../examples/introcs-python/dict_algorithms/patterns.py
   :language: python
   :start-after: # start: grouping
   :end-before: # end: grouping

Output:

.. code-block:: none

   {'a': ['apple', 'ant'], 'b': ['banana', 'berry'], 'c': ['car', 'cat']}

The general grouping pattern is:

.. code-block:: none

   for item in data:
       key = some_property(item)
       if key not in groups:
           groups[key] = []
       groups[key].append(item)

``setdefault`` is a convenient shorthand:

.. code-block:: python

   groups = {}
   for w in words:
       groups.setdefault(w[0], []).append(w)

.. index:: dict; invert, dict comprehension; key-value swap

Reversing a Dictionary
-----------------------

Swap keys and values. This works correctly only when values are unique and hashable.
Run it and try adding a duplicate value to see what happens:

.. try_examples::
   :height: 220px

   >>> grades = {"A": 90, "B": 80, "C": 70}
   >>> reversed_grades = {v: k for k, v in grades.items()}
   >>> print(reversed_grades)
   {90: 'A', 80: 'B', 70: 'C'}

If values are not unique, later entries overwrite earlier ones during the reversal.

.. index:: dict; merge operator |, dict.update(); merge, Python 3.9; dict merge

Merging Dictionaries
---------------------

Python 3.9+ provides the merge operator ``|``. Run it and edit the dictionaries:

.. try_examples::
   :height: 240px

   >>> a = {"x": 1, "y": 2}
   >>> b = {"y": 3, "z": 4}
   >>> c = a | b
   >>> print(c)
   {'x': 1, 'y': 3, 'z': 4}

If both dictionaries share a key, the right-hand dictionary wins. For older Python:

.. code-block:: python

   c = dict(a)
   c.update(b)

.. index:: dict.get(); safe access, KeyError; avoiding with get

Safe Access with ``.get()``
----------------------------

Use ``.get()`` to avoid ``KeyError`` when a key may not exist. Run it, then try
adding ``"mode"`` to ``config`` and see how the result changes:

.. try_examples::
   :height: 220px

   >>> config = {"debug": True}
   >>> mode = config.get("mode", "production")
   >>> print(mode)
   production

.. index:: nested dictionaries, hierarchical data; dict

Nested Dictionaries
--------------------

Dictionaries can hold other dictionaries, allowing hierarchical data. Run it and
try reaching the science score:

.. try_examples::
   :height: 260px

   >>> student = {
   ...     "name": "Alice",
   ...     "scores": {"math": 90, "science": 85}
   ... }
   >>> print(student["scores"]["math"])
   90

.. index:: dict algorithms; lists of dicts, index by unique field; O(1) lookup, frequency count; list of dicts

Algorithms on Lists of Dictionaries
-------------------------------------

A list of dictionaries is a common format for tabular data (CSV rows, JSON records,
API responses). Several dictionary algorithms apply naturally to this structure.

**Frequency count over a field:**

.. literalinclude:: ../../examples/introcs-python/dict_algorithms/patterns.py
   :language: python
   :start-after: # start: list_of_dicts
   :end-before: # end: list_of_dicts

Output:

.. code-block:: none

   {30: 2, 25: 1}

**Index by a unique field** (convert list → dictionary for O(1) lookup). Run it
and look up a different person:

.. try_examples::
   :height: 280px

   >>> people = [
   ...     {"name": "Alice", "age": 30},
   ...     {"name": "Bob", "age": 25},
   ...     {"name": "Cara", "age": 30},
   ... ]
   >>> index = {p["name"]: p for p in people}
   >>> print(index["Alice"])
   {'name': 'Alice', 'age': 30}

**Group records by a field:**

.. code-block:: python

   by_age = {}
   for p in people:
       by_age.setdefault(p["age"], []).append(p)

.. index:: group_by_length; example, dict; group by length

Group by Length (Practice)
--------------------------

Implement a function that groups words by their length:

.. literalinclude:: ../../examples/introcs-python/dict_algorithms/patterns.py
   :language: python
   :start-after: # start: group_by_length
   :end-before: # end: group_by_length

Output:

.. code-block:: none

   {3: ['tea', 'jam', 'bag'], 2: ['to'], 5: ['apple']}

.. index:: dict algorithms; real-world uses, analytics pipelines; dict, search index; dict

Real-World Applications
-----------------------

Dictionary algorithms appear throughout software:

- **Analytics pipelines** — counting events, computing statistics.
- **Search indexes** — mapping words to the documents that contain them.
- **Grouping and categorization** — organizing records by department, date,
  or status.
- **Summarizing survey data** — counting responses per answer option.

Recognizing when a problem maps to one of these patterns is a key skill in Python
programming.

Exercises
---------

1. Count the frequency of each character in the string ``"mississippi"``.
2. Given a list of words, filter out any word with fewer than four letters and
   return a dictionary mapping the remaining words to their lengths.
3. Given a list of student records (each a dictionary with ``name``, ``grade``,
   and ``score``), group them by ``grade``.
4. Reverse the dictionary ``{"red": 1, "green": 2, "blue": 3}``. What happens
   if two keys share the same value?
5. Merge two configuration dictionaries so that values in the second dictionary
   take priority over the first.
6. Write a function ``top_n(counts, n)`` that returns the ``n`` most frequent
   items from a frequency dictionary as a sorted list of ``(item, count)`` tuples.
