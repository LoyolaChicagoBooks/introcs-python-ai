.. index:: dictionary, dict; syntax, dict; key-value
   ACM-IEEE CS2013; SDF3 Fundamental Data Structures
   ACM-IEEE CS2023; SDF3 Fundamental Data Structures

.. _Dictionary-Syntax:

Dictionary Syntax
=================

A *dictionary* maps *keys* to *values*.  Given a key, you can look up its
associated value in constant time — like looking up a word in a reference
book.

Creating Dictionaries
---------------------

.. index:: dict; literal, dict; constructor

Use braces with ``key: value`` pairs.  Run this and edit the entries:

.. try_examples::
   :height: 260px

   >>> e2sp = {"one": "uno", "two": "dos", "three": "tres"}
   >>> word_count = {}       # empty dict
   >>> ages = {"Alice": 30, "Bob": 25}
   >>> e2sp
   {'one': 'uno', 'two': 'dos', 'three': 'tres'}
   >>> word_count
   {}
   >>> ages
   {'Alice': 30, 'Bob': 25}

.. index:: dict(); constructor

You can also use ``dict()`` with keyword arguments.  Try it live:

.. try_examples::
   :height: 220px

   >>> e2sp = dict(one="uno", two="dos", three="tres")
   >>> e2sp
   {'one': 'uno', 'two': 'dos', 'three': 'tres'}

Accessing and Modifying Entries
---------------------------------

.. index:: dict; access, dict; update

Use square brackets to get or set a value by key.  Run this and edit the
keys and values:

.. try_examples::
   :height: 260px

   >>> e2sp = {"one": "uno", "two": "dos", "three": "tres"}
   >>> e2sp["one"]
   'uno'
   >>> e2sp["four"] = "cuatro"   # add new entry
   >>> e2sp["two"] = "DOS"       # update existing entry
   >>> e2sp
   {'one': 'uno', 'two': 'DOS', 'three': 'tres', 'four': 'cuatro'}

.. index:: KeyError, dict.get(); default value

Accessing a key that does not exist raises a ``KeyError``.  Use
``dict.get(key, default)`` to avoid the exception.  Try both forms live:

.. try_examples::
   :height: 260px

   >>> e2sp = {"one": "uno", "two": "dos", "three": "tres"}
   >>> e2sp.get("five", "not found")
   'not found'
   >>> e2sp.get("one", "not found")
   'uno'
   >>> e2sp["five"]
   Traceback (most recent call last):
       ...
   KeyError: 'five'

Membership Test
---------------

.. index:: in; dict key

Use ``in`` to test whether a key is present.  Try it live:

.. try_examples::
   :height: 240px

   >>> e2sp = {"one": "uno", "two": "dos", "three": "tres"}
   >>> "three" in e2sp
   True
   >>> "seven" in e2sp
   False

Removing Entries
----------------

.. index:: del; dict, dict.pop()

- ``del d[key]`` removes the entry (raises ``KeyError`` if absent).
- ``d.pop(key)`` removes and returns the value; accepts an optional default.
- ``d.clear()`` removes all entries.

Run this and watch the dictionary shrink:

.. try_examples::
   :height: 260px

   >>> e2sp = {"one": "uno", "two": "dos", "three": "tres"}
   >>> del e2sp["two"]
   >>> removed = e2sp.pop("three", None)
   >>> removed
   'tres'
   >>> len(e2sp)         # number of remaining entries
   1
   >>> e2sp
   {'one': 'uno'}

Iterating Over a Dictionary
-----------------------------

.. index:: dict.keys(), dict.values(), dict.items(), for; dict

A dictionary can be iterated several ways.  Run this and edit the loops:

.. try_examples::
   :height: 360px

   >>> e2sp = {"one": "uno", "two": "dos", "three": "tres"}
   >>> for key in e2sp:               # iterate over keys (insertion order)
   ...     print(key, "->", e2sp[key])
   ...
   one -> uno
   two -> dos
   three -> tres
   >>> for key in e2sp.keys():        # explicit keys view
   ...     print(key)
   ...
   one
   two
   three
   >>> for val in e2sp.values():      # values view
   ...     print(val)
   ...
   uno
   dos
   tres
   >>> for key, val in e2sp.items():  # key-value pairs
   ...     print(f"{key}: {val}")
   ...
   one: uno
   two: dos
   three: tres

Build and modify a dictionary below.  Try adding keys, updating values,
and calling ``.get()`` with a missing key to see how it differs from
``[]`` access:

.. try_examples::
   :height: 320px

   >>> e2sp = {"one": "uno", "two": "dos", "three": "tres"}
   >>> e2sp["four"] = "cuatro"             # add a new entry
   >>> e2sp["one"]
   'uno'
   >>> e2sp.get("five", "not found")       # safe lookup with default
   'not found'
   >>> "three" in e2sp
   True
   >>> for key, val in e2sp.items():
   ...     print(f"{key}: {val}")
   ...
   one: uno
   two: dos
   three: tres
   four: cuatro

Key Type Restriction
--------------------

.. index:: dict; key must be immutable

Dictionary keys must be *immutable* — strings, numbers, and tuples are
valid keys; lists are not.  This restriction exists because of how hash
tables work (see :ref:`Dictionary-Efficiency`).
