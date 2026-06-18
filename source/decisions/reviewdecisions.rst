Chapter Review Questions
========================

1. Two similar-looking operators.

   a.  What does ``=`` do in Python?
   b.  What does ``==`` do?
   c.  Give a one-line example of each.

2. Python's Boolean operators.

   a.  Name all three.

3. What is printed?  Predict the output first, then press **Try it live** to
   check:

   .. try_examples::
      :height: 300px

      >>> x = 7
      >>> if x > 5:
      ...     print("big")
      ...
      big
      >>> if x > 10:
      ...     print("very big")
      ... else:
      ...     print("not very big")
      ...
      not very big

4. Short-circuit evaluation.

   a.  What does *short-circuit evaluation* mean?
   b.  Give an example where it prevents a runtime error.

5. Rewrite this nested ``if`` using a single condition with ``and``:

   .. code-block:: python

      if age >= 18:
          if has_id:
              print("Entry allowed.")

6. What is the bug in this code?  Fix it.

   .. code-block:: python

      score = 85
      if score >= 90:
          grade = "A"
      if score >= 80:
          grade = "B"
      if score >= 70:
          grade = "C"
      print(grade)

7. Write a function ``absolute_value(x)`` using an ``if``/``else``
   statement that returns the absolute value of ``x`` without using
   ``abs()``.

8. Write a function ``sign(x)`` that returns ``1`` if ``x > 0``,
   ``-1`` if ``x < 0``, and ``0`` if ``x == 0``.

9. Write a function ``is_leap_year(year)`` that returns ``True`` if
   ``year`` is a leap year.  A year is a leap year if it is divisible
   by 4, *except* centuries (divisible by 100) are not leap years, *unless*
   they are also divisible by 400.

10. What does this expression evaluate to, and what type does it produce?
    Predict first, then press **Try it live** to confirm:

    .. try_examples::
       :height: 220px

       >>> "pass" if 75 >= 60 else "fail"
       'pass'
       >>> type("pass" if 75 >= 60 else "fail")
       <class 'str'>
