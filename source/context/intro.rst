.. index::
   ACM-IEEE CS2013; SP1 Social Context
   ACM-IEEE CS2023; SP1 Social Context

.. _resources-online:

Resources Online
================

This book is designed for the introductory computer science course at Loyola
University Chicago.  The materials are available to all on the web.

.. note::

   For all work in this course, install Python 3 and use the command-line
   tools.  The basic workflow is:

   1. Write a ``.py`` file in a text editor (Vim or Emacs recommended).
   2. Run it from the terminal::

         python3 filename.py

   You can also experiment interactively by typing ``python3`` at the
   terminal to enter the interactive shell.

*  The course example repository will contain all example programs referenced
   in the book.  Download or clone it and keep it alongside your work.

*  `python.org <https://www.python.org>`_ is the official Python website.
   It includes documentation for the standard library and language reference.

*  We recommend learning a terminal-based editor such as `Vim <https://www.vim.org>`_
   or `GNU Emacs <https://www.gnu.org/software/emacs/>`_.  Mastering one of these
   builds habits — editing, navigating, and running code — that transfer directly
   to any command-line environment.  `Visual Studio Code
   <https://code.visualstudio.com>`_ is an acceptable alternative, but you will get
   more out of it once you are comfortable working between an editor and the shell.

.. index:: Python; interactive shell
   REPL

The Interactive Shell
---------------------

Python provides an interactive shell (also called a REPL, for
Read-Evaluate-Print Loop) that lets you type expressions and see their
values immediately.  Start it by typing ``python3`` at your terminal:

.. code-block:: none

   $ python3
   Python 3.12.0 (default, ...)
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

Type any expression and press Enter::

   >>> 2 + 3
   5
   >>> "Hello, world!"
   'Hello, world!'

This is very useful for experimenting with small pieces of code.  We will use
the ``>>>`` prompt throughout the book to show interactive examples.

To exit the shell, type ``quit()`` or press Ctrl-D.

.. index:: JupyterLite, Pyodide, Try it live, browser; running Python

.. _try-it-live:

Running Code in Your Browser
----------------------------

Many examples in this book sit behind a **Try it live ▶** button.  Click it and
the example turns into a live, editable Python cell that runs right on the page
— no installation, no account, and nothing sent to a server.  This is powered by
`JupyterLite <https://jupyterlite.readthedocs.io>`_ and
`Pyodide <https://pyodide.org>`_ (a build of Python that runs inside your web
browser).  Edit the code, run it again, and experiment freely; your changes are
not saved, so reload the page to start over.  The first run takes a few seconds
while Python loads.

Here is a tiny example to try right now.  Click **Try it live**, run it, then
change the greeting and run it again — the date and time will be the moment
*you* run it:

.. try_examples::
   :height: 240px

   >>> print("Hello, world!")
   Hello, world!
   >>> from datetime import datetime
   >>> print("The current date and time is", datetime.now())
   The current date and time is 2026-06-18 09:15:42.531809

The time shown above is only a sample; running the cell prints your computer's
current date and time.  This in-browser execution has limits — examples that
read files or use the network cannot run there — so for coursework you will
still use a local Python installation, as described above.

.. _alt-formats:

Alternate Formats
-----------------

This book is available in HTML, PDF, and EPUB formats.  See the download
links at the top of each page.
