.. index:: input, user input, argparse, command line interface, interactive programs
   ACM-IEEE CS2013; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2023; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2013; SE3 Tools and Environments
   ACM-IEEE CS2023; SE3 Tools and Environments

.. _User-Input-Overview:

User Input
==========

.. note::
   *Source:* Contributed by PhD students in COMP 501 at Loyola University Chicago.

Up to this point our programs have worked with data written directly into the code.
But most real applications must react to information that changes while the program
is running — data typed by a user, arguments provided at startup, or values read
from a file. Python provides three primary ways to receive this kind of external
input.

.. index:: input(); overview, input; always returns string

The ``input()`` Function
------------------------

``input()`` is the simplest and most direct way to receive information from a user
during program execution. When called, the program pauses and waits for the user to
type a response and press Enter. The function always returns a **string**, so numeric
input must be converted to the appropriate type.

.. literalinclude:: ../../examples/introcs-python/user_input/calculator.py
   :language: python

Testing for valid input often involves checking whether the provided data can be
converted to the expected type. Because users can type anything, it is good practice
to wrap conversions in a ``try/except`` block and guide users back toward valid
responses when they provide something unexpected.

``input()`` is ideal for simple, conversational programs where a human guides
execution step by step.

.. index:: argparse; CLI overview, command line interface; argparse

Command-Line Interfaces with ``argparse``
------------------------------------------

The ``argparse`` module allows you to create a command-line interface (CLI) that
accepts input *before* the program starts running. Unlike ``input()``, which pauses
mid-execution, a CLI lets users define all inputs on the command line when they
launch the script.

.. code-block:: python

   # A greeting program with a command-line interface
   import argparse

   parser = argparse.ArgumentParser(description="A simple greeting program.")
   parser.add_argument("--name", type=str, required=True,
                       help="The name of the person to greet")
   args = parser.parse_args()

   print(f"Hello, {args.name}! Welcome to the Python CLI demo.")

Run it from the terminal:

.. code-block:: none

   python greet.py --name Alice

Output:

.. code-block:: none

   Hello, Alice! Welcome to the Python CLI demo.

``argparse`` can enforce data types, require certain arguments, restrict input to a
set of valid choices, and automatically generate ``--help`` output. A CLI is
especially useful for automation and scripting — running a program repeatedly with
different inputs without editing the source code each time.

.. index:: file reading; overview, open(); with block

Reading Data from Files
-----------------------

Many programs need to work with data stored outside the program itself — text
documents, configuration files, or large datasets. Reading from files allows a
program to process persistent information without requiring user input for every
value.

Python's built-in ``open()`` function provides access to files for reading or
writing. The recommended pattern uses a ``with`` block, which ensures the file is
closed automatically even if an error occurs.

.. code-block:: python

   # Read a text file and count its lines and words
   file_path = "example.txt"

   try:
       with open(file_path, "r", encoding="utf-8") as file:
           contents = file.read()
           lines = contents.splitlines()
           words = contents.split()

           print(f"File: {file_path}")
           print(f"Number of lines: {len(lines)}")
           print(f"Number of words: {len(words)}")
   except FileNotFoundError:
       print(f"The file '{file_path}' was not found.")

The modern ``pathlib.Path`` class offers an object-oriented alternative:

.. code-block:: python

   from pathlib import Path

   path = Path("example.txt")
   if path.exists():
       contents = path.read_text(encoding="utf-8")
       print(f"Number of lines: {len(contents.splitlines())}")

Both approaches achieve the same result. ``pathlib`` is often considered cleaner for
complex path manipulation (joining directories, checking extensions, listing files),
while ``open()`` is familiar and widely used.

.. index:: input; method selection, input; comparison table

Choosing the Right Input Method
--------------------------------

+------------------+--------------------------------------------------+
| Method           | When to use it                                   |
+==================+==================================================+
| ``input()``      | Simple, interactive, step-by-step programs.      |
+------------------+--------------------------------------------------+
| ``argparse``     | Automation, scripting, or tools for other users. |
+------------------+--------------------------------------------------+
| File reading     | Processing large or persistent datasets.         |
+------------------+--------------------------------------------------+

These three methods form the foundation of all interactive and data-driven programs.
Mastering them prepares you for more advanced topics such as data validation, control
structures, and error handling.

Exercises
---------

1. Write a program that asks the user for their name and age, then prints a
   personalized message. Handle the case where the age is not a valid integer.
2. Write a script using ``argparse`` that accepts a filename and an optional
   ``--lines`` flag. When ``--lines`` is provided, print only the first N lines
   of the file; otherwise print the entire file.
3. Write a program that reads a file of numbers (one per line), computes their
   sum and average, and skips any lines that are not valid numbers.
4. Compare ``input()`` and ``argparse``: for each of the following scenarios,
   state which approach you would use and why.

   - A script that runs nightly on a server to process log files.
   - A small program that quizzes a student on vocabulary words.
   - A utility that converts temperatures from Celsius to Fahrenheit.
