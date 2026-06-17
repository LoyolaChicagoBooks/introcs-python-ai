.. index:: JupyterLite, Pyodide, interactive Python, browser REPL, replite

.. _Interactive-Python-Overview:

Interactive Python in the Browser
==================================

.. note::

   This chapter demonstrates `jupyterlite-sphinx
   <https://jupyterlite-sphinx.readthedocs.io>`_, an extension that embeds a
   fully interactive Python interpreter — powered by
   `Pyodide <https://pyodide.org>`_ and WebAssembly — directly in the page.
   No server is required; computation happens inside your browser.

Every code example in this book can be read and studied in static form.
This chapter shows something different: live, editable Python that runs
*in the page itself*.  You can modify the code, press **Shift-Enter** (or
click **Run**), and see the result immediately — no installation, no account,
no server.

The technology behind this is **Pyodide**, a port of CPython compiled to
WebAssembly.  The `jupyterlite-sphinx` extension builds a self-contained
JupyterLite site alongside the HTML book and surfaces it through the
``replite`` directive.  Everything stays on your machine; no code is sent
to a remote server.

.. note::

   Pyodide runs a real CPython interpreter in the browser, so almost all
   pure-Python code works identically to what you would type at a local
   terminal.     The main limitations are: no real filesystem access, no
   ``subprocess``, and network requests are sandboxed by the browser.
   Examples in the :ref:`fileread` and :ref:`Internet-Data` chapters
   therefore cannot run in this environment.

.. index:: replite directive

A First Calculation
--------------------

The widget below is a live Python REPL.  The opening code is pre-loaded;
press **Shift-Enter** to run it, then edit the values and run again.

.. replite::
   :kernel: python
   :height: 200px
   :prompt: Run

   # Arithmetic in Python
   width = 12
   height = 7
   area = width * height
   print(f"Area: {area}")

.. index:: f-string; interactive, for loop; interactive

Loops and f-Strings
--------------------

The ``for`` loop and f-strings you learned in earlier chapters work exactly
the same way here.

.. replite::
   :kernel: python
   :height: 250px
   :prompt: Run

   fruits = ["apple", "banana", "cherry"]
   for i, fruit in enumerate(fruits, start=1):
       print(f"{i}. {fruit}")

.. index:: function; interactive, def

Defining Functions
-------------------

You can define and call functions in the REPL just as you would in a script.

.. replite::
   :kernel: python
   :height: 280px
   :prompt: Run

   def greet(name: str) -> str:
       """Return a personalised greeting."""
       return f"Hello, {name}! Welcome to Python."

   for name in ["Alice", "Bob", "Carol"]:
       print(greet(name))

.. index:: list comprehension; interactive

List Comprehensions
--------------------

.. replite::
   :kernel: python
   :height: 220px
   :prompt: Run

   squares = [x ** 2 for x in range(1, 11)]
   print("Squares 1-10:", squares)

   evens = [x for x in range(20) if x % 2 == 0]
   print("Even numbers < 20:", evens)

.. index:: numpy; interactive, Pyodide; numpy

Using numpy
------------

Pyodide ships popular scientific packages.  ``numpy`` and ``matplotlib``
are available without any installation step.

.. replite::
   :kernel: python
   :height: 250px
   :prompt: Run

   import numpy as np

   data = np.array([4, 9, 16, 25, 36])
   print("Data:", data)
   print("Square roots:", np.sqrt(data))
   print("Mean:", np.mean(data))
   print("Std dev:", np.std(data))

.. index:: matplotlib; interactive, plot; browser

Plotting with matplotlib
-------------------------

The REPL can render matplotlib figures inline.  Run the cell below to
produce a simple plot.

.. replite::
   :kernel: python
   :height: 400px
   :prompt: Run

   import numpy as np
   import matplotlib.pyplot as plt

   x = np.linspace(0, 2 * np.pi, 200)
   y = np.sin(x)

   fig, ax = plt.subplots()
   ax.plot(x, y, label="sin(x)")
   ax.set_xlabel("x")
   ax.set_ylabel("y")
   ax.set_title("Sine Wave")
   ax.legend()
   plt.show()

.. index:: replite; sandbox, WebAssembly; Python

How It Works
-------------

When you first interact with a REPL widget, the page downloads the Pyodide
runtime (approximately 10 MB, cached after the first visit).  A real Python
interpreter then starts inside the browser tab.  Each widget shares a kernel
within the page, so variables defined in one cell are visible in later cells
on the same page — exactly like a Jupyter notebook session.

The source for this chapter is a plain RST file using the ``.. replite::``
directive provided by `jupyterlite-sphinx`.  The directive accepts:

- ``:kernel:`` — the kernel name (``python`` uses Pyodide)
- ``:height:`` — CSS height of the embedded widget
- ``:prompt:`` — label of the "run" button shown before the kernel loads

The content of the directive is the Python code pre-loaded into the cell.

Limitations
^^^^^^^^^^^

Because the interpreter runs inside a browser sandbox:

- File I/O (``open()``, ``pathlib.Path``) works only for in-memory paths;
  it cannot read files from your local hard drive.
- ``subprocess``, ``socket``, and most networking is unavailable.
- Packages not bundled with Pyodide require a ``micropip.install()`` call
  and must be pure-Python or pre-compiled for WebAssembly.

For interactive code that requires real files or network access, use a
local Python installation or a cloud environment such as GitHub Codespaces.
