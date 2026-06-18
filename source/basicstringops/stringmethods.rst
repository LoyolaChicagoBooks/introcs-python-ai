.. index:: string; method, string; immutability

.. _string-methods-length:

String Methods and Length
=========================

Strings in Python are *objects* — they bundle data (the characters) with
operations (methods).  You call a method with dot notation:
``string_value.method_name(arguments)``.

All string methods return *new* strings.  Strings are **immutable**: calling
a method never changes the original string.  Try it live:

.. try_examples::
   :height: 300px

   >>> s = "hello"
   >>> s.upper()
   'HELLO'
   >>> s             # unchanged
   'hello'
   >>> s = s.upper() # reassign to get the new value
   >>> s
   'HELLO'

.. index:: len()

``len()``
---------

``len(s)`` returns the number of characters in ``s``.  It is a built-in
function, not a method.  Try it live:

.. try_examples::
   :height: 220px

   >>> len("coding")
   6
   >>> len("")
   0

.. index:: str.upper(), str.lower()

Case Conversion
---------------

Python provides methods for converting between upper and lower case, capitalising the first word, or title-casing every word.  Try it live:

.. try_examples::
   :height: 280px

   >>> "Hello World".upper()
   'HELLO WORLD'
   >>> "Hello World".lower()
   'hello world'
   >>> "hello world".capitalize()
   'Hello world'
   >>> "hello world".title()
   'Hello World'

.. index:: str.strip(), str.lstrip(), str.rstrip()

Stripping Whitespace
--------------------

``strip()`` removes leading and trailing whitespace (spaces, tabs, newlines).
Try it live:

.. try_examples::
   :height: 240px

   >>> "  hello  ".strip()
   'hello'
   >>> "  hello  ".lstrip()   # left side only
   'hello  '
   >>> "  hello  ".rstrip()   # right side only
   '  hello'

This is especially useful when reading user input or lines from a file.

.. index:: str.find(), str.index()

Finding Substrings
------------------

``find(sub)`` returns the index of the first occurrence of ``sub``, or
``-1`` if it is not found.  Try it live:

.. try_examples::
   :height: 220px

   >>> "Bonjour".find("jo")
   3
   >>> "Bonjour".find("xyz")
   -1

``index(sub)`` works the same way but raises a ``ValueError`` instead of
returning ``-1`` when not found.

.. index:: str.startswith(), str.endswith()

Testing Start and End
---------------------

``startswith()`` and ``endswith()`` return ``True`` or ``False`` and are commonly used in ``if`` statements to filter or classify strings.  Try it live:

.. try_examples::
   :height: 240px

   >>> "hello.py".endswith(".py")
   True
   >>> "hello.py".startswith("he")
   True
   >>> "hello.py".startswith("lo")
   False

These return ``True`` or ``False`` and are often used in ``if`` statements.

.. index:: str.replace()

Replacing Substrings
--------------------

``replace(old, new)`` returns a copy of the string with every occurrence of
``old`` replaced by ``new``.  Try it live:

.. try_examples::
   :height: 220px

   >>> "It was the best of times.".replace("best", "worst")
   'It was the worst of times.'
   >>> "aababc".replace("ab", "X")
   'aXXc'

An optional third argument limits how many replacements to make.  Try it live:

.. try_examples::
   :height: 200px

   >>> "aababc".replace("ab", "X", 1)
   'aXabc'

.. index:: str.split(), str.join()

Splitting and Joining
---------------------

``split()`` breaks a string into a list of words, splitting on whitespace by
default.  Try it live:

.. try_examples::
   :height: 200px

   >>> "one two three".split()
   ['one', 'two', 'three']

Pass a delimiter to split on something specific.  Try it live:

.. try_examples::
   :height: 220px

   >>> "a,b,c".split(",")
   ['a', 'b', 'c']
   >>> "2024-05-01".split("-")
   ['2024', '05', '01']

``join()`` is the inverse: it assembles a list of strings into one string,
inserting a separator between each pair.  Try it live:

.. try_examples::
   :height: 220px

   >>> ", ".join(["Alice", "Bob", "Carol"])
   'Alice, Bob, Carol'
   >>> "-".join(["2024", "05", "01"])
   '2024-05-01'

.. index:: string; method summary

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 30 50

   * - Expression
     - Result
   * - ``len(s)``
     - Number of characters
   * - ``s.upper()``
     - Uppercase copy
   * - ``s.lower()``
     - Lowercase copy
   * - ``s.capitalize()``
     - First letter uppercase, rest lower
   * - ``s.title()``
     - Title-case copy
   * - ``s.strip()``
     - Remove leading/trailing whitespace
   * - ``s.find(sub)``
     - Index of first ``sub`` (-1 if absent)
   * - ``s.startswith(pre)``
     - ``True`` if ``s`` begins with ``pre``
   * - ``s.endswith(suf)``
     - ``True`` if ``s`` ends with ``suf``
   * - ``s.replace(old, new)``
     - Copy with ``old`` → ``new``
   * - ``s.split(sep)``
     - List of substrings split by ``sep``
   * - ``sep.join(lst)``
     - Join list with ``sep`` between items

String Methods Exercise
-----------------------

Predict the output, then run the cell to check:

.. try_examples::
   :height: 360px

   >>> w = "quickly"
   >>> print(len(w))
   7
   >>> print(w[len(w) - 2])
   l
   >>> print(w[3:5])
   ck
   >>> print(w[2:])
   ickly
   >>> print(w.find("ti"))
   -1
   >>> print(w.find("ick"))
   2
   >>> k = w.find("c")
   >>> print(k, w[k], w[k - 3], w[k:])
   3 c q ckly
