Chapter Review Questions
========================

1. What is printed by this fragment?  Predict first, then run the cell to check:

   .. try_examples::
      :height: 300px

      >>> s = "question"
      >>> print(len(s))
      8
      >>> print(s[2])
      e
      >>> print(s[2:5])
      est
      >>> print(s[3:])
      stion
      >>> print(s.find("ti"))
      4
      >>> print(s.find("to"))
      -1

2. What is printed by this fragment?  Predict first, then run the cell to check:

   .. try_examples::
      :height: 200px

      >>> s = "Word"
      >>> s.upper()
      'WORD'
      >>> print(s)
      Word

3. What is printed by this fragment?  Predict first, then run the cell to check:

   .. try_examples::
      :height: 200px

      >>> a = "hi"
      >>> b = a.upper()
      >>> print(a + b)
      hiHI

4. Strings and mutability.

   a.  Are strings mutable or immutable?
   b.  What does that mean in practice when you call a method like
       ``s.upper()``?

5. Both ``s.find(sub)`` and ``s.index(sub)`` search for a substring.
   What is the difference in their behavior when the substring is *not*
   present in ``s``?

6. Write an expression that extracts the last three characters of a string
   ``s``, without using a literal index number.

7. What does ``s[::-1]`` do?

8. Write a function ``count_vowels(s)`` that returns the number of vowel
   characters (``a``, ``e``, ``i``, ``o``, ``u``, case-insensitive) in
   string ``s``.

9. What is printed by this fragment?  Predict first, then run the cell to check:

   .. try_examples::
      :height: 220px

      >>> parts = "2024-05-01".split("-")
      >>> print(parts)
      ['2024', '05', '01']
      >>> print("-".join(parts))
      2024-05-01

10. Write a function ``title_case(s)`` that returns ``s`` converted to title
    case (first letter of each word capitalized) without using the built-in
    ``str.title()`` method.  Use ``split()`` and ``join()``.
