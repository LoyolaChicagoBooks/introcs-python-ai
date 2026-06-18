.. index:: string

Strings, Part I
===============

A *string* is a sequence of characters.  Strings are one of the most
commonly used types in Python.

.. index:: string literal, quotes

String Literals
---------------

You can write a string literal using either single quotes or double quotes.
They are equivalent.  Using double quotes inside single-quoted strings (and
vice versa) avoids backslashes, and *triple quotes* — either ``"""`` or
``'''`` — let a string span multiple lines.  Try editing these:

.. index:: triple-quoted string, multiline string

.. try_examples::
   :height: 320px

   >>> 'Hello'
   'Hello'
   >>> "Hello"
   'Hello'
   >>> 'She said, "Hello."'
   'She said, "Hello."'
   >>> "It's a fine day."
   "It's a fine day."
   >>> poem = """Roses are red,
   ... Violets are blue."""
   >>> print(poem)
   Roses are red,
   Violets are blue.

.. index:: string concatenation, string repetition

String Operations
-----------------

The ``+`` operator *concatenates* (joins) two strings, and the ``*`` operator
*repeats* a string.  Try changing the words and counts below:

.. try_examples::
   :height: 280px

   >>> "Hello, " + "world!"
   'Hello, world!'
   >>> first = "Ada"
   >>> last = "Lovelace"
   >>> full = first + " " + last
   >>> full
   'Ada Lovelace'
   >>> "ha" * 3
   'hahaha'
   >>> "-" * 20
   '--------------------'

.. index:: len()

String Length
-------------

``len()`` returns the number of characters in a string.  Try it with your own
words:

.. try_examples::
   :height: 220px

   >>> len("Hello")
   5
   >>> len("")
   0
   >>> len("Ada Lovelace")
   12

.. index:: string; immutability

Strings are Immutable
---------------------

Strings cannot be changed after they are created.  You can create a *new*
string based on an old one, but you cannot modify the original.  Trying to
assign to a single character raises an error; instead, build a new string.
Try it:

.. try_examples::
   :height: 300px

   >>> s = "Hello"
   >>> s[0] = "J"       # This will cause an error
   Traceback (most recent call last):
       ...
   TypeError: 'str' object does not support item assignment
   >>> s = "J" + s[1:]
   >>> s
   'Jello'

Slicing and indexing are covered in the Basic String Operations chapter.

.. index:: str(), type conversion

Converting to String
---------------------

Use ``str()`` to convert other types to strings.  Try it:

.. try_examples::
   :height: 260px

   >>> str(42)
   '42'
   >>> str(3.14)
   '3.14'
   >>> "The answer is " + str(42)
   'The answer is 42'

Note that you *cannot* concatenate a string and a number directly — doing so
raises a ``TypeError``:

.. try_examples::
   :height: 220px

   >>> "The answer is " + 42
   Traceback (most recent call last):
       ...
   TypeError: can only concatenate str (not "int") to str

You must convert first with ``str()``, or use an f-string (see :ref:`fstrings`).
