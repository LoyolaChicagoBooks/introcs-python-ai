.. index:: dict; examples, word count example, Counter

.. _Dictionary-Examples:

Dictionary Examples
===================

Word Count
----------

.. index:: word count, dict; word count

Counting how often each word appears in a text is a classic dictionary
application.  We process a string word by word, updating a count for each
word seen.  Run it on a short phrase to see counts accumulate for repeated
words, then edit the text:

.. try_examples::
   :height: 360px

   >>> def word_count(text):
   ...     counts = {}
   ...     for word in text.lower().split():
   ...         word = word.strip(".,!?;:\"'")   # remove punctuation
   ...         if word:
   ...             counts[word] = counts.get(word, 0) + 1
   ...     return counts
   ...
   >>> text = "four score and seven years ago our fathers four score"
   >>> counts = word_count(text)
   >>> for word in sorted(counts):
   ...     print(f"{word:10s}  {counts[word]}")
   ...
   ago         1
   and         1
   fathers     1
   four        2
   our         1
   score       2
   seven       1
   years       1

``counts.get(word, 0)`` returns the current count or 0 if the word has
not been seen yet — a cleaner alternative to checking ``word in counts``
first.

.. index:: dict comprehension

Inverting a Dictionary
-----------------------

.. index:: dict; invert

To build a reverse lookup (value → key) from a one-to-one dictionary, run
this:

.. try_examples::
   :height: 240px

   >>> e2sp = {"one": "uno", "two": "dos", "three": "tres"}
   >>> sp2e = {v: k for k, v in e2sp.items()}
   >>> sp2e
   {'uno': 'one', 'dos': 'two', 'tres': 'three'}

This dict comprehension is the dictionary analogue of a list comprehension.

Using ``collections.Counter``
------------------------------

.. index:: Counter, collections.Counter

Python's ``collections.Counter`` is a specialised dict subclass that
counts hashable objects automatically.  It is cleaner than writing the
accumulation loop by hand.  Run it live:

.. try_examples::
   :height: 260px

   >>> from collections import Counter
   >>> text = "four score and seven years ago our fathers four score"
   >>> counts = Counter(text.lower().split())
   >>> counts.most_common(3)
   [('four', 2), ('score', 2), ('and', 1)]

``most_common(n)`` returns the n most frequent elements as a list of
``(element, count)`` tuples.

Grouping Data
--------------

.. index:: dict; grouping

A dictionary whose values are lists is a natural way to group items.  Run
this and edit the word list:

.. try_examples::
   :height: 340px

   >>> words = ["apple", "ant", "bear", "bee", "cat"]
   >>> by_letter = {}
   >>> for word in words:
   ...     letter = word[0]
   ...     if letter not in by_letter:
   ...         by_letter[letter] = []
   ...     by_letter[letter].append(word)
   ...
   >>> for letter in sorted(by_letter):
   ...     print(f"{letter}: {by_letter[letter]}")
   ...
   a: ['apple', 'ant']
   b: ['bear', 'bee']
   c: ['cat']

.. index:: dict.setdefault()

``dict.setdefault(key, default)`` can simplify the inner ``if``:

.. code-block:: python

   by_letter.setdefault(letter, []).append(word)
