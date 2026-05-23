.. index:: terminal, shell, command line, stdin, stdout, stderr, redirection,
           pipe, sys.argv, argparse, cat, touch, cp, mv, rm, echo, less, grep,
           find, chmod, chown, ps, top, kill, file permissions, process management
   ACM-IEEE CS2013; SE3 Tools and Environments
   ACM-IEEE CS2023; SE3 Tools and Environments

.. _Terminal-Overview:

The Terminal
============

.. note::
   *Source:* Contributed by PhD students in COMP 501 at Loyola University Chicago.

Throughout this course you have been running Python programs by clicking a "Run"
button in an IDE or executing code in an interactive shell. Now we explore another
powerful way to interact with your programs: the **terminal**.

The terminal may seem intimidating at first — a text-based window with no buttons to
click. But it is one of the most important tools in a programmer's toolkit, and
learning to use it will make you more capable as a developer.

.. index:: terminal emulator, shell; definition, bash, zsh

Terminal vs. Shell
------------------

People often use "terminal" and "shell" interchangeably, but they refer to different
things.

- **Terminal** (or terminal emulator) — the window on your screen where text
  appears. On macOS this is the Terminal app; on Windows, Command Prompt or
  PowerShell; on Linux, GNOME Terminal or similar.
- **Shell** — the program running *inside* the terminal that reads your commands
  and tells the operating system to execute them. Common shells include ``bash``,
  ``zsh``, ``fish``, and PowerShell.

Think of it this way: the terminal is the video-call window (Zoom, Teams) — just
the frame. The shell is the person you are talking to — the part that actually
understands and responds.

Why Programmers Use the Terminal
---------------------------------

Even though graphical interfaces are available, experienced programmers often
prefer the terminal for several reasons:

- **Speed** — typing a command is faster than navigating menus. Renaming 100 files
  with a graphical interface means 100 click-rename cycles; with the terminal, a
  single command handles all of them at once.
- **Precision** — you can express exactly what you want, with no ambiguity.
- **Automation** — sequences of commands can be saved in scripts and run
  automatically, including your Python programs.
- **Remote work** — the terminal works the same whether you are on your laptop or
  connected to a server on the other side of the world.
- **Universal skill** — terminal commands are similar or identical across operating
  systems; learning them once pays dividends everywhere.

Opening Your Terminal
---------------------

**macOS**: Press ``Command + Space``, type ``Terminal``, press Enter. Or find it
in ``Applications > Utilities > Terminal``.

**Windows**: Press the Windows key, type ``PowerShell`` or ``cmd``, press Enter.

**Linux**: Press ``Ctrl + Alt + T`` on most distributions.

When the terminal opens you will see a **prompt** — the shell's signal that it is
ready for a command. The prompt typically ends with ``$`` on macOS/Linux or ``>``
on Windows.

Essential Commands
------------------

``pwd`` — print working directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shows your current location in the file system.

.. code-block:: none

   $ pwd
   /Users/yourname/Documents

``ls`` — list contents
^^^^^^^^^^^^^^^^^^^^^^^

Shows what is in your current directory (use ``dir`` on Windows Command Prompt).

.. code-block:: none

   $ ls
   homework.txt    python_projects    essay.docx

``cd`` — change directory
^^^^^^^^^^^^^^^^^^^^^^^^^^

Moves you to a different directory.

.. code-block:: none

   cd python_projects    # move into a subdirectory
   cd ..                 # move up one level
   cd ~                  # move to your home directory

``mkdir`` — make directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a new directory. In the terminal, **no news is good news** — if the command
succeeds, you just get the prompt back.

.. code-block:: none

   mkdir my_project

``whoami`` — show current user
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prints your account name — useful when you are working on a shared system or switching between users:

.. code-block:: none

   $ whoami
   yourname

``cat`` — display file contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prints the contents of a file to the terminal. You can view one file or several at once.

.. code-block:: none

   $ cat notes.txt

   $ cat file1.txt file2.txt

``touch`` — create empty files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates one or more empty files. If the file already exists, ``touch`` updates its
timestamp without changing the contents.

.. code-block:: none

   $ touch hello.py
   $ touch file1.py file2.py file3.py

``cp`` — copy files and directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copies a file to a new location. Use ``-r`` (recursive) to copy an entire directory.

.. code-block:: none

   $ cp notes.txt notes_backup.txt
   $ cp -r my_project my_project_backup

``mv`` — move or rename
^^^^^^^^^^^^^^^^^^^^^^^^

Moves a file to a different location, or renames it when the destination is in the
same directory.

.. code-block:: none

   $ mv old_name.py new_name.py
   $ mv script.py ~/Documents/

``rm`` — remove files and directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deletes a file permanently — there is no Recycle Bin from the terminal. Use ``-r``
to remove a directory and everything inside it.

.. code-block:: none

   $ rm temp.txt
   $ rm -r old_project

``echo`` — print text
^^^^^^^^^^^^^^^^^^^^^^

Prints a message to the terminal. Frequently used in scripts and to inspect variable
values.

.. code-block:: none

   $ echo "Hello, world!"
   $ echo "Current user: $USER"

``less`` — page through a file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Opens a file one screen at a time. Press ``Space`` to advance, ``b`` to go back,
and ``q`` to quit. Unlike ``cat``, ``less`` is comfortable for long files.

.. code-block:: none

   $ less long_file.txt

``grep`` — search text
^^^^^^^^^^^^^^^^^^^^^^^

Searches for a pattern inside a file and prints matching lines. ``grep`` is one of
the most useful commands for exploring code and log files.

.. code-block:: none

   $ grep "def " my_script.py
   $ grep -i "error" server.log

The ``-i`` flag makes the search case-insensitive.

``find`` — locate files by name or property
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searches a directory tree for files matching criteria such as name, size, or
modification date.

.. code-block:: none

   $ find . -name "*.py"
   $ find ~/Documents -name "report.txt"

File Permissions
-----------------

Every file on a Unix-like system has an owner and a set of permissions that control
who may read, write, or execute it.

``chmod`` — change permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The numeric mode ``755`` means the owner can read, write, and execute; everyone else
can read and execute.

.. code-block:: none

   $ chmod 755 my_script.py

``chown`` — change ownership
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transfers ownership of a file to a different user or group. This is most commonly
needed on shared servers.

.. code-block:: none

   $ chown alice:staff my_script.py

Process Management
------------------

A **process** is a running program. The terminal gives you tools to observe and
control processes.

``ps`` — list running processes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shows a snapshot of the processes currently running in your terminal session.

.. code-block:: none

   $ ps

``top`` — live process monitor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Displays all processes in real time, sorted by CPU usage. Press ``q`` to quit.

.. code-block:: none

   $ top

``kill`` — terminate a process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a signal to a process, usually to stop it. Replace ``PID`` with the numeric
process ID shown by ``ps`` or ``top``.

.. code-block:: none

   $ kill 1234

.. index:: stdin, stdout, stderr, standard streams, redirection

Standard Streams
----------------

When a program runs, it communicates through three standard channels:

- **stdin** (standard input) — where the program reads input. When you type into a
  running program, it comes through stdin.
- **stdout** (standard output) — where the program sends normal output. Python's
  ``print()`` writes to stdout.
- **stderr** (standard error) — where the program sends error messages. Having a
  separate channel for errors lets you handle them independently from normal output.

.. code-block:: none

   User Input → [stdin] → Your Program → [stdout] → Normal Output
                                       ↳ [stderr] → Error Messages

Here is a Python script that writes to all three:

.. code-block:: python

   import sys

   print("This goes to stdout")
   sys.stdout.write("This also goes to stdout\n")
   sys.stderr.write("This goes to stderr\n")

   user_input = input("Type something: ")
   print(f"You typed: {user_input}")

.. index:: command redirection, shell; redirection, pipe, stdout; redirection,
           stdin; redirection, stderr; redirection, here document

Command Redirection
-------------------

Standard streams can be connected to files and to other commands.  This is
called **redirection**.  Redirection is one reason terminal commands are so
powerful: a command does not need to know whether its input came from the
keyboard, a file, or another program.

The most common redirection operators are:

.. list-table::
   :header-rows: 1

   * - Operator
     - Meaning
   * - ``>``
     - Send stdout to a file, replacing the file if it already exists.
   * - ``>>``
     - Send stdout to a file, appending to the end if it already exists.
   * - ``<``
     - Read stdin from a file instead of the keyboard.
   * - ``2>``
     - Send stderr to a file.
   * - ``|``
     - Send stdout from one command into stdin of another command.

Using a Pipe
^^^^^^^^^^^^

The vertical bar symbol, ``|``, is called a **pipe**.  It connects the output of
one command to the input of another command.

For example, to check whether a file called ``hello.py`` appears in the current
directory, send the output of ``ls`` into ``grep``:

.. code-block:: none

   $ ls | grep hello.py

If ``hello.py`` exists, its name is printed.  If it does not exist, nothing is
printed.  The ``ls`` command writes a list of filenames to stdout; ``grep`` reads
that list from stdin and prints only matching lines.

Writing Output to a File
^^^^^^^^^^^^^^^^^^^^^^^^

The ``>`` operator sends stdout to a file.  This makes it possible to create a
short file without opening an editor:

.. code-block:: none

   $ echo 'print("Hello, world!")' > hello.py

The outer single quotes protect the inner double quotes, so the shell passes the
Python statement to ``echo`` as one piece of text.  After running the command,
``hello.py`` contains:

.. code-block:: python

   print("Hello, world!")

You can run the new program immediately:

.. code-block:: none

   $ python hello.py
   Hello, world!

Be careful with ``>``.  If the file already exists, the shell replaces its
contents.  Use ``>>`` when you want to append instead:

.. code-block:: none

   $ echo 'print("Goodbye!")' >> hello.py

Reading Input from a File
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``<`` operator sends a file into a program's stdin.  Suppose
``name_reader.py`` contains:

.. code-block:: python

   name = input("Name: ")
   print(f"Hello, {name}!")

Create a small input file:

.. code-block:: none

   $ echo "Ada" > name.txt

Then run the program with stdin redirected from the file:

.. code-block:: none

   $ python name_reader.py < name.txt
   Name: Hello, Ada!

The program still calls ``input()``, but the input comes from ``name.txt``
instead of the keyboard.

Capturing Error Messages
^^^^^^^^^^^^^^^^^^^^^^^^

Because stderr is separate from stdout, you can save error messages without
mixing them with normal output.  The ``2>`` operator redirects stderr:

.. code-block:: none

   $ python missing_file.py 2> errors.txt

If the program prints a traceback or another error message, that message is
written to ``errors.txt``.  Normal output still appears in the terminal unless
you redirect stdout too.

Creating Several Lines with a Here Document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A **here document** lets you provide several lines of text to a command.  The
``cat`` command normally copies stdin to stdout.  Combined with ``>``, it can
create a short Python file:

.. code-block:: none

   $ cat > channels.py <<'END'
   import sys

   print("This goes to stdout")
   sys.stdout.write("This also goes to stdout\\n")
   sys.stderr.write("This goes to stderr\\n")

   user_input = input("Type something: ")
   print(f"You typed: {user_input}")
   END

The word ``END`` marks where the input stops.  It is not written into the file.
Quoting it as ``'END'`` tells the shell not to interpret special characters
inside the text.

This technique is useful for creating very small programs before you have
learned a terminal editor such as Vim or Emacs.  For larger programs, use a real
editor so you can revise the file safely.

Running Python Scripts from the Terminal
-----------------------------------------

Create a file called ``hello_terminal.py``:

.. code-block:: python

   print("Hello from the terminal!")
   print("This script is running successfully.")

Then run it:

.. code-block:: none

   python hello_terminal.py

(Use ``python3`` if your system requires it.)

.. index:: exit code, sys.exit(), shell; exit code

Exit Codes
^^^^^^^^^^

When a program ends it reports an **exit code** back to the shell:

- ``0`` means success.
- Any non-zero value means failure.

.. code-block:: python

   import sys

   choice = input("Should this program succeed? (yes/no): ")

   if choice.lower() == "yes":
       print("Success!")
       sys.exit(0)
   else:
       print("Failure!")
       sys.exit(1)

Check the exit code after running:

.. code-block:: none

   # macOS/Linux
   echo $?

   # Windows PowerShell
   echo $LASTEXITCODE

.. index:: sys.argv, command line arguments; sys.argv

Command Line Arguments with ``sys.argv``
-----------------------------------------

Sometimes you want to give a program information *before* it starts running. Python's
``sys.argv`` is a list that holds:

- ``sys.argv[0]`` — the script name
- ``sys.argv[1]``, ``sys.argv[2]``, … — any extra words typed after the script name

.. code-block:: python

   import sys

   print("Arguments:", sys.argv)

   for i, arg in enumerate(sys.argv):
       print(f"Argument {i}: {arg}")

Run it:

.. code-block:: none

   python show_arguments.py hello world 123

Output:

.. code-block:: none

   Arguments: ['show_arguments.py', 'hello', 'world', '123']
   Argument 0: show_arguments.py
   Argument 1: hello
   Argument 2: world
   Argument 3: 123

Here is a script that uses ``sys.argv`` to greet a user:

.. code-block:: python

   import sys

   if len(sys.argv) < 2:
       print("Error: please provide your name.")
       print("Usage: python greet.py YourName")
       sys.exit(1)

   name = sys.argv[1]
   print(f"Hello, {name}!")
   sys.exit(0)

.. index:: argparse; ArgumentParser, CLI; argparse, --help flag

Professional CLI Programs with ``argparse``
--------------------------------------------

``sys.argv`` is simple but limited — it provides no automatic help, no validation,
and no support for optional flags. Python's ``argparse`` module solves all of this.

.. literalinclude:: ../../examples/introcs-python/terminal/greet_argparse.py
   :language: python

Try:

.. code-block:: none

   python greet_argparse.py Alice
   python greet_argparse.py Alice -n 5
   python greet_argparse.py --help

``argparse`` automatically generates a ``--help`` message that lists all arguments,
their types, and their descriptions — essential for any tool that others will use.

Here is a more complete example — a file search tool:

.. literalinclude:: ../../examples/introcs-python/terminal/search_file.py
   :language: python

Try:

.. code-block:: none

   python search_file.py story.txt dragon
   python search_file.py story.txt dragon -i
   python search_file.py story.txt dragon -i -n
   python search_file.py --help

Exercises
---------

1. Open your terminal and run ``pwd``, ``ls``, and ``whoami``. What do they tell
   you?
2. Create a directory called ``practice``, move into it, create two subdirectories
   inside it, and then navigate back to the parent.
3. Write a script ``greet.py`` that takes a name as a command line argument and
   prints ``Hello, <name>!``. Exit with code ``1`` if no name is provided.
4. Extend the script using ``argparse`` to also accept an optional ``--times``
   flag that controls how many times the greeting is printed.
5. Write a script ``process_numbers.py`` that:

   - Accepts one or more numbers as positional arguments.
   - Supports optional flags ``--sum``, ``--average``, ``--max``, and ``--min``.
   - Uses ``argparse`` and exits with a non-zero code if any argument is not a
     valid number.
