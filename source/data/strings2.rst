.. index:: escape sequence

String Special Cases
====================

.. index:: escape sequences; table

Escape Sequences
----------------

Some characters cannot be typed directly inside a string literal.  Python
uses *escape sequences* — a backslash followed by a character — to represent
them:

.. list-table::
   :header-rows: 1
   :widths: 15 45

   * - Sequence
     - Meaning
   * - ``\\``
     - Literal backslash
   * - ``\'``
     - Single quote
   * - ``\"``
     - Double quote
   * - ``\n``
     - Newline (line feed)
   * - ``\t``
     - Tab
   * - ``\r``
     - Carriage return
   * - ``\0``
     - Null character

Press **Try it live** to run these and watch the escapes take effect:

.. try_examples::
   :height: 260px

   >>> print("Line one\nLine two")
   Line one
   Line two
   >>> print("Column 1\tColumn 2")
   Column 1	Column 2
   >>> print("She said, \"Hello.\"")
   She said, "Hello."

.. index:: raw string

Raw Strings
-----------

If you need a string that contains many backslashes — such as a Windows file
path — a *raw string* treats backslashes as literal characters.  Prefix the
opening quote with ``r``:

Try editing the path below and see that the backslashes stay literal:

.. try_examples::
   :height: 220px

   >>> path = r"C:\Users\student\Documents"
   >>> print(path)
   C:\Users\student\Documents

Without the ``r``, ``\U``, ``\s``, and ``\D`` would be interpreted as escape
sequences (and either produce unexpected characters or errors).

.. index:: multiline string, triple-quoted string

Multiline Strings
-----------------

Triple-quoted strings can span multiple lines and preserve all whitespace,
including newlines:

.. code-block:: python

   message = """Dear student,

   Welcome to Introduction to Computer Science.

   Regards,
   The Department"""
   print(message)

Output:

.. code-block:: none

   Dear student,

   Welcome to Introduction to Computer Science.

   Regards,
   The Department

.. index:: docstring

Triple-quoted strings are also used as *docstrings* — documentation attached
to functions and classes.  We will see those in the Functions chapter.

.. index:: string; in operator

Testing for Substrings
-----------------------

The ``in`` operator tests whether one string is a substring of another:

Try changing the words below to test other substrings:

.. try_examples::
   :height: 240px

   >>> "cat" in "concatenate"
   True
   >>> "dog" in "concatenate"
   False
   >>> "not" not in "certainly"
   True
