.. index:: hardware, software, CPU, RAM, operating system, memory hierarchy, process, cloud computing, data representation, boolean logic, ICT literacy
   ACM-IEEE CS2013; AR1 Digital Logic and Digital Systems
   ACM-IEEE CS2023; AR1 Digital Logic and Digital Systems
   ACM-IEEE CS2013; AR/MachineLevel Machine Level Representation of Data
   ACM-IEEE CS2023; AR/MachineLevel Machine Level Representation of Data
   ACM-IEEE CS2013; AR/MemoryArch Memory Architectures
   ACM-IEEE CS2023; AR/MemoryArch Memory Architectures
   ACM-IEEE CS2013; DS/BasicLogic Discrete Structures Basic Logic
   ACM-IEEE CS2023; DS/BasicLogic Discrete Structures Basic Logic
   ACM-IEEE CS2013; CN/Intro ICT Literacy Foundations
   ACM-IEEE CS2023; CN/Intro ICT Literacy Foundations
   ACM-IEEE CS2013; OS/Overview Operating Systems Overview
   ACM-IEEE CS2023; OS/Overview Operating Systems Overview

.. _Hardware-And-Software:

Hardware and Software
=====================

.. note::
   *Source:* Originally contributed by PhD students in COMP 501 at Loyola University
   Chicago. The Memory Hierarchy, Processes, and Types of Computer Systems sections
   draw on material from the companion
   `Operating Systems <https://os.cs.luc.edu>`__ and
   `CS Curricula <https://curricula.cs.luc.edu>`__ sites.

Every computer system is built on two inseparable layers: **hardware**, the physical
components you can touch, and **software**, the instructions that tell the hardware
what to do. Understanding both layers — and how they work together — gives you a
mental model that will serve you throughout your programming career.

.. index:: hardware; components, CPU; role, RAM; role, motherboard, storage; SSD HDD, input devices, output devices

What Is Hardware?
-----------------

**Hardware** consists of the tangible components of a computer system. These components
perform computation, store data, interact with the outside world, and support all of
those functions.

The core hardware components are:

- **CPU (Central Processing Unit)** — the "brain" of the computer. It executes
  instructions from software, performs calculations, and makes decisions.
- **Memory (RAM)** — short-term, fast storage. RAM holds data and programs
  *currently in use* so the CPU can access them quickly. Its contents are lost
  when power is off.
- **Storage (SSD/HDD)** — long-term storage for files, applications, and the
  operating system. Data persists even when the power is off.
- **Input devices** — let data and commands enter the system. Examples: keyboard,
  mouse, touchscreen, camera, microphone.
- **Output devices** — show or send results back to the user. Examples: monitor,
  printer, speakers.
- **Supporting hardware** — power supplies, batteries, cooling fans, and network
  interfaces (USB, Wi-Fi) that keep the system stable and connected.

All major components are connected through the **motherboard**, which acts as the
circulatory system of the computer, carrying power and signals between parts.

.. index:: memory hierarchy, cache; CPU, registers; CPU, RAM; speed, storage; speed
   ACM-IEEE CS2013; AR/MemoryArch Memory Architectures
   ACM-IEEE CS2023; AR/MemoryArch Memory Architectures
   ACM-IEEE CS2013; AR/MultiLevel Multi-Level Machine Organization
   ACM-IEEE CS2023; AR/MultiLevel Multi-Level Machine Organization

The Memory Hierarchy
--------------------

The hardware components that store data are not equal — they differ dramatically in
speed and size. This tradeoff is captured by the **memory hierarchy**, a ladder that
runs from the fastest (and smallest) storage to the slowest (and largest):

- **Registers** — a handful of locations inside the CPU itself that hold the
  values being computed right now.  Registers are the fastest storage that
  exists, but a typical processor has fewer than a hundred of them.
- **Cache** — a small pool of high-speed memory (L1, L2, and L3 levels) built
  onto the processor chip.  The CPU automatically copies recently used data
  here so it does not have to reach out to RAM every time.
- **RAM** (main memory) — where your running program and all of its data live
  while the machine is on.  Much larger than cache but noticeably slower.
- **SSD** (solid-state drive) — flash-based secondary storage for files,
  databases, and the operating system at rest.  Much faster than a spinning
  disk but still orders of magnitude slower than RAM.
- **HDD** (hard disk drive) — traditional spinning magnetic storage offering
  large capacity at low cost, but with mechanical seek times that make it
  the slowest form of local storage in everyday use.
- **Tape** — removable magnetic tape cartridges used for archival backups and
  long-term storage.  Sequential access only; far cheaper per gigabyte than
  any disk, but retrieving data can take minutes.

The table below puts concrete numbers on these differences.  Latencies are
approximate and vary by hardware generation, but the *ratios* between levels
are remarkably stable [DeanNorvig]_ [HennessyPatterson2024]_.

.. list-table:: Approximate memory hierarchy latencies
   :header-rows: 1
   :widths: 22 28 22

   * - Level
     - Typical latency
     - Order of magnitude
   * - Registers
     - < 1 ns
     - 10⁰ ns
   * - L1 cache
     - ~1 ns
     - 10⁰ ns
   * - L2 cache
     - ~4 ns
     - 10⁰ ns
   * - L3 cache
     - ~15 ns
     - 10¹ ns
   * - RAM
     - ~100 ns
     - 10² ns
   * - NVMe SSD
     - ~100,000 ns (100 µs)
     - 10⁵ ns
   * - HDD
     - ~10,000,000 ns (10 ms)
     - 10⁷ ns
   * - Tape
     - ~10,000,000,000 ns (10 s)
     - 10¹⁰ ns

Each level is roughly 10–100× slower than the one above it but offers far more
capacity. When the CPU needs a value it checks the cache first, then RAM, and only
falls back to storage as a last resort.

.. figure:: memory_hierarchy.png
   :alt: The memory hierarchy pyramid, showing registers at the top (fastest, smallest)
         down through cache, RAM, and disk storage at the bottom (slowest, largest)
   :align: center
   :width: 80%

   The memory hierarchy pyramid.  Speed increases and capacity decreases as you
   move toward the top.
   `Image <https://commons.wikimedia.org/wiki/File:ComputerMemoryHierarchy.svg>`_
   by Blog.Knatten.org, `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_.

You can see the hierarchy in action from Python. The ``sys`` module reports how much
RAM a Python object occupies, and ``time`` lets you measure how long operations take:

.. literalinclude:: ../../examples/introcs-python/hardware/memory_timing.py
   :language: python

Sample output (exact numbers vary by machine):

.. code-block:: none

   RAM used by list: 8,000,056 bytes
   RAM  time: 0.0049 s
   Disk time: 0.1268 s

Running this will show the disk read taking many times longer than the in-memory sum,
even on a fast SSD. The gap is larger still on a traditional hard drive. Keeping
frequently used data in RAM — rather than re-reading it from disk every time — is one
of the most important performance principles in all of computing.

.. index:: data representation, binary, hexadecimal, octal, bits, bytes
   ACM-IEEE CS2013; AR/MachineLevel Machine Level Representation of Data
   ACM-IEEE CS2023; AR/MachineLevel Machine Level Representation of Data
   ACM-IEEE CS2013; DS/Data Discrete Structures: Data Representation
   ACM-IEEE CS2023; DS/Data Discrete Structures: Data Representation

Data Representation
--------------------

Every piece of data a computer stores or processes — numbers, text, images, sound —
is ultimately represented as **bits**: individual 0s and 1s. Eight bits make a
**byte**. A single byte can represent 256 different values (0–255).

Humans usually write numbers in **decimal** (base 10, digits 0–9). Computers work
internally in **binary** (base 2, digits 0 and 1). Two other bases appear constantly
in computing:

- **Octal** (base 8) — historically used in Unix file permissions.
- **Hexadecimal** (base 16, digits 0–9 and A–F) — a compact shorthand for binary
  since one hex digit represents exactly four bits.

Python has built-in functions for converting between bases:

.. code-block:: python

   num = 42
   print(f"Decimal:     {num}")
   print(f"Binary:      {bin(num)}")
   print(f"Octal:       {oct(num)}")
   print(f"Hexadecimal: {hex(num)}")

Output:

.. code-block:: none

   Decimal:     42
   Binary:      0b101010
   Octal:       0o52
   Hexadecimal: 0x2a

You can also convert back: ``int('0b101010', 2)``, ``int('0x2a', 16)``, and
``int('0o52', 8)`` all return ``42``. The prefix (``0b``, ``0o``, ``0x``) tells
Python which base to use.

**Horner's Method: converting to any base**

Python's ``bin``, ``oct``, and ``hex`` only handle bases 2, 8, and 16. The classic
algorithm for converting a decimal integer to *any* base uses repeated division:
divide by the base, record the remainder as the next digit, and repeat until the
quotient reaches zero. Reading the remainders in reverse gives the result. This is
known as **Horner's method** (or successive division).

For bases up to 16 we can represent each digit as a single character (``0``–``9``
then ``A``–``F``). For larger bases there are not enough single characters, so we
represent each digit as a decimal number separated by colons — exactly the way
hours, minutes, and seconds are written for base 60.

.. literalinclude:: ../../examples/introcs-python/hardware/base_conversion.py
   :language: python

Output:

.. code-block:: none

   101010
   52
   2A
   -101010
   FF
   60
   202
   -60
   42
   1:30
   1:0:0
   1:1:1

Base 60 (**sexagesimal**) was invented by the Babylonians around 2000 BCE and
is still with us today: 60 seconds in a minute, 60 minutes in an hour, 360
degrees in a circle (6 × 60). The colon-separated output mirrors the familiar
``hours:minutes:seconds`` notation — which is itself a base-60 representation.
Base 7 is less common in practice but illustrates that the same algorithm works
for any base with no changes to the code.

.. index:: boolean logic, logic gates, AND, OR, NOT, XOR, truth table, De Morgan's laws
   ACM-IEEE CS2013; DS/BasicLogic Discrete Structures: Basic Logic
   ACM-IEEE CS2023; DS/BasicLogic Discrete Structures: Basic Logic
   ACM-IEEE CS2013; AR/ALU Digital Logic and Digital Systems
   ACM-IEEE CS2023; AR/ALU Digital Logic and Digital Systems

Boolean Logic and Logic Gates
------------------------------

At the hardware level, the CPU is built from billions of tiny **logic gates** — each
one performs a simple operation on bits. The fundamental gates are:

- **AND** — output is 1 only if *both* inputs are 1.
- **OR** — output is 1 if *at least one* input is 1.
- **NOT** — inverts the input: 0 becomes 1, 1 becomes 0.
- **XOR** (exclusive OR) — output is 1 if the inputs *differ*; 0 if they are the same.

All computation — arithmetic, comparison, branching — is ultimately built from
combinations of these gates. Python exposes the same operations through its boolean
operators:

.. code-block:: python

   a = True
   b = False

   print(f"a AND b:  {a and b}")
   print(f"a OR b:   {a or b}")
   print(f"NOT a:    {not a}")
   print(f"a XOR b:  {a != b}")   # exclusive OR: true when inputs differ

Output:

.. code-block:: none

   a AND b:  False
   a OR b:   True
   NOT a:    False
   a XOR b:  True

A **truth table** enumerates every possible combination of inputs and the
corresponding output. Here is one for AND:

.. code-block:: python

   print(f"{'A':<6} {'B':<6} {'A AND B'}")
   for a in [False, True]:
       for b in [False, True]:
           print(f"{str(a):<6} {str(b):<6} {a and b}")

Output:

.. code-block:: none

   A      B      A AND B
   False  False  False
   False  True   False
   True   False  False
   True   True   True

**De Morgan's Laws** are two identities that relate AND, OR, and NOT. They come
up constantly when simplifying logical conditions in code:

.. code-block:: python

   a, b = True, False

   # NOT (a AND b)  ==  (NOT a) OR  (NOT b)
   print(not (a and b) == (not a or not b))   # True

   # NOT (a OR b)   ==  (NOT a) AND (NOT b)
   print(not (a or b)  == (not a and not b))  # True

You will use boolean logic every time you write an ``if`` statement. The chapter on
:ref:`Simple Conditions <Simple-Conditions>` covers this in depth.

.. index:: software; categories, system software, application software, utility software, drivers; hardware

What Is Software?
-----------------

**Software** consists of the programs and instructions that run on hardware. Software
tells the hardware what to do, in what order, and how to respond to inputs.

There are three main categories of software:

- **System software** — manages the basic operations of the computer.

  - *Operating systems*: Windows, macOS, Linux, Android, iOS.
  - *Drivers*: small programs that let the OS communicate with specific hardware
    (e.g., a printer driver or graphics driver).

- **Application software** — programs that people interact with to accomplish tasks.
  Examples: web browsers, word processors, games, messaging apps, music players.

- **Utility software** — supporting tools that maintain and optimize the system.
  Examples: antivirus tools, backup utilities, file compression, disk cleanup.

.. index:: systems programming languages, C language, C++ language, Java language, Rust language, assembly language, Ada language, Go language, Python; as high-level language
   ACM-IEEE CS2013; PL/Languages Programming Languages: Language Translation and Execution
   ACM-IEEE CS2023; PL/Languages Programming Languages: Language Translation and Execution

Programming Languages Across the Stack
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Not all software is written in the same language. Different layers of the stack
call for different tools:

- **Assembly** — one step above raw machine code. Specific to a CPU architecture.
  Used for bootloaders, firmware, and performance-critical inner loops. Gives
  complete control but is tedious and non-portable.

- **C** — the dominant systems language since the 1970s. The Linux kernel, macOS
  core, and most of the internet's infrastructure are written in C. Fast, portable,
  and close to the hardware — but the programmer manages memory manually.

- **C++** — extends C with object-oriented features. Used in operating systems,
  game engines, browsers (Chrome, Firefox), and real-time systems.

- **Java** — compiles to bytecode that runs on the Java Virtual Machine (JVM),
  making programs portable across platforms without recompilation. Java manages
  memory automatically through garbage collection. It dominates enterprise
  backend systems and Android app development, and influenced languages like
  C# and Kotlin.

- **Rust** — a modern systems language designed for memory safety without a
  garbage collector. Increasingly used in OS components, browsers, and
  infrastructure where C/C++ were previously the only options.

- **Ada** — developed by the U.S. Department of Defense for safety-critical and
  mission-critical systems: avionics, defense, and medical devices.

- **Go** — a modern, compiled language from Google designed for simplicity and
  performance. Its efficiency and built-in concurrency support have made it popular
  for networking, cloud infrastructure, and server-side systems programming.

- **Python** — the language you are learning in this course — sits at the opposite
  end of the spectrum from assembly. It is interpreted, memory-managed, and highly
  expressive. Python trades raw performance for readability and development speed,
  making it ideal for data analysis, scripting, automation, and applications.
  Many systems are built with a fast C/Rust core and a Python layer on top.

.. index:: input-process-output model, hardware; software interaction

How Hardware and Software Work Together
---------------------------------------

The simplest model for understanding how a computer processes information is:

.. code-block:: none

   Input → Processing → Output

- **Input**: data or commands entering the system (keypress, tap, voice command).
- **Processing**: the CPU and RAM executing instructions and manipulating data.
- **Output**: the result shown or sent back to the user (text on screen, sound,
  a printed page).

Here is a concrete walkthrough — pressing the "A" key on a keyboard:

1. **Input**: the keyboard's hardware sends an electrical signal for that key.
2. **Driver/OS**: a keyboard driver translates the signal into a code the OS
   understands, then routes it to the active application.
3. **Processing (CPU, RAM)**: the CPU runs the word processor's code that inserts
   the letter. The document and cursor position are held in RAM.
4. **Output**: the OS updates the display, and the monitor shows the letter A.

.. index:: operating system; role, OS; resource manager, OS; service provider, OS; translator
   ACM-IEEE CS2013; OS/Overview Operating Systems Overview
   ACM-IEEE CS2023; OS/Overview Operating Systems Overview

The Role of the Operating System
---------------------------------

The operating system (OS) is the invisible coordinator that sits between applications
and hardware. It plays three roles simultaneously:

- **Resource manager** — schedules CPU time, allocates RAM, manages storage, and
  handles devices so programs do not conflict with one another.
- **Service provider** — offers common services (file dialogs, network access,
  security) so each application does not have to build them from scratch.
- **Translator** — applications do not talk directly to hardware. They ask the OS
  instead ("draw this window", "save this file"), and the OS uses drivers to
  translate those requests into hardware signals.

.. index:: process; definition, PID, os module; getpid, os module; getppid, process; parent
   ACM-IEEE CS2013; OS/Overview Operating Systems Overview
   ACM-IEEE CS2023; OS/Overview Operating Systems Overview
   ACM-IEEE CS2013; OS/Processes Processes and Threads
   ACM-IEEE CS2023; OS/Processes Processes and Threads

Processes: Programs in Motion
------------------------------

A **program** is a set of instructions stored on disk — it is inert until the OS
loads and runs it. When that happens the OS creates a **process**: a running instance
of the program with its own slice of RAM, its own open files, and a unique
**process ID (PID)**. The same program can produce many processes at once (think of
opening several browser tabs).

Every process on a Unix system has a parent — the process that created it. When
you run a Python script from the terminal, your shell is the parent. Python itself
is the child process. You can inspect this directly:

.. code-block:: python

   import os

   print(f"This script's PID:    {os.getpid()}")
   print(f"Parent process's PID: {os.getppid()}")

Sample output (the exact numbers vary each run):

.. code-block:: none

   This script's PID:    48271
   Parent process's PID: 48202

The OS is responsible for creating, scheduling, and eventually cleaning up every
process on the system. When your Python script finishes — or crashes — the OS
reclaims the memory and file handles that process was using.

You can also ask Python to start a new child process of its own using the
``subprocess`` module:

.. code-block:: python

   import subprocess

   result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
   print(result.stdout)

.. code-block:: none

   Python 3.12.x

Here ``subprocess.run`` asks the OS to create a new process that runs
``python3 --version``, waits for it to finish, and returns its output. This is
exactly how the terminal works when you type a command — the shell is a process
that spawns child processes for each command you run.

.. index:: computer systems; types, personal computer, distributed system, cloud computing, quantum computing
   ACM-IEEE CS2013; CN/Overview Networking and Communication Introduction
   ACM-IEEE CS2023; CN/Overview Networking and Communication Introduction
   ACM-IEEE CS2013; AR/MultiLevel Multi-Level Machine Organization
   ACM-IEEE CS2023; AR/MultiLevel Multi-Level Machine Organization

Types of Computer Systems
--------------------------

So far we have described a single desktop or laptop. In practice, "a computer system"
can take many forms:

**Personal computers and workstations**
   The machines most students use for coursework: laptops, desktops, and tablets.
   One user, one machine, general-purpose tasks.

**Servers and data centers**
   Powerful machines (or racks of machines) that run continuously and serve many
   users at once — hosting websites, databases, and applications. The computer in
   your pocket communicates with servers constantly.

**Distributed systems**
   Multiple computers networked together that cooperate to solve a problem or
   provide a service. No single machine has all the data or does all the work.
   The internet itself is a distributed system.

   Every machine on a network has an identity you can inspect from Python:

   .. code-block:: python

      import socket
      print(socket.gethostname())

**Cloud computing**
   Renting computing resources — servers, storage, databases — over the internet
   rather than owning physical hardware. AWS, Google Cloud, and Microsoft Azure
   are the dominant providers. When you push code to GitHub or stream music, you
   are using cloud infrastructure.

**High-performance computing (HPC) and clusters**
   Hundreds or thousands of processors working in parallel on a single large
   computation: weather forecasting, protein folding, physics simulations. These
   systems divide a problem into pieces and solve them simultaneously.

**Quantum computers**
   Rather than bits (0 or 1), quantum computers use *qubits* that can exist in
   multiple states simultaneously. This makes certain problems — such as breaking
   encryption or simulating molecules — tractable in ways classical computers
   cannot match. Quantum computing is still an emerging field, but it represents
   a fundamental shift in how computation can be performed.

.. note::
   The Python programs in this book run on a personal computer. But the skills
   you build here — writing clear, correct programs — transfer directly to
   servers, cloud functions, and distributed systems. The language is the same;
   only the scale changes.

.. index:: ICT literacy, digital citizenship, online safety, information literacy
   ACM-IEEE CS2013; CN/Intro Information and Communication Technology Literacy: Foundations
   ACM-IEEE CS2023; CN/Intro Information and Communication Technology Literacy: Foundations

Information and Communication Technology Literacy
--------------------------------------------------

The ACM/IEEE curricula include a knowledge unit called *ICT Literacy: Foundations*
that is relevant from the very first course. It describes the competencies every
computing student should develop — not just programming skills, but the broader
habits of a responsible technology user:

- **Fundamental concepts** — understanding what hardware, software, networks, and
  the internet are and how they relate. This chapter covers the hardware and
  software side; networking appears later in the book.

- **Operational skills** — being able to use common tools (terminal, text editor,
  file system, browser), manage files and directories, and navigate an operating
  system. The Terminal chapter addresses this directly.

- **Online communication** — understanding email, forums, collaborative platforms
  (GitHub, shared documents), and how to use them appropriately in a professional
  and academic context.

- **Digital citizenship** — awareness of the ethical, cultural, and legal issues
  around computing: intellectual property, privacy, and the social impact of
  technology. These themes recur throughout the course.

- **Online safety and security** — using strong, unique passwords; enabling
  two-factor authentication; recognizing phishing; practicing safe browsing. These
  are not optional extras — they are professional baseline skills.

- **Problem-solving with ICT** — using search effectively, reading documentation,
  troubleshooting hardware and software issues methodically. Learning to *find*
  answers is as important as knowing answers.

.. note::
   These competencies are harder to grade than code — but they matter just as much.
   A programmer who writes correct Python but falls for a phishing email, ignores
   licensing, or cannot navigate a terminal is not yet a complete computing
   professional.

.. index:: hardware; analogies, software; analogies

Metaphors for Hardware and Software
-------------------------------------

Concrete analogies can make these abstractions easier to remember:

- **Body and mind**: hardware is the body (organs, muscles); software is the mind
  (thoughts, decisions, instructions). Neither is useful without the other.
- **Kitchen and recipe**: hardware is the kitchen (stove, pots, utensils); software
  is the recipe (steps and instructions). The same kitchen can produce many dishes
  by following different recipes.
- **Instruments and sheet music**: hardware is the instruments; software is the
  score. Change the music, and the same instruments produce a different performance.

Exercises
---------

1. List five hardware components found in a smartphone. For each one, identify
   whether it is an input device, output device, processing unit, or storage unit.
2. Classify each of the following as system software, application software, or
   utility software: macOS, Spotify, an antivirus scanner, a printer driver,
   a web browser, a disk defragmenter.
3. Trace the Input → Processing → Output steps that occur when you tap the "Play"
   button in a music app.
4. In your own words, explain what an operating system does. Use the traffic-cop
   or translator metaphors if they help.
5. Draw the memory hierarchy as a triangle with the fastest/smallest storage at
   the top. Label each level with an approximate size (bytes, kilobytes,
   gigabytes, terabytes) and a representative access time.
6. Run the memory hierarchy Python example from this chapter. Record the RAM time
   and disk time. How many times faster is RAM access on your machine?
7. Run the process identity example (``os.getpid()`` / ``os.getppid()``). Open
   your operating system's process viewer (Activity Monitor on macOS, Task Manager
   on Windows, ``top`` on Linux) and find Python in the list. Does the PID match?
8. Classify each of the following as a personal computer, server, distributed
   system, or cloud service: your laptop, Gmail, a university's web server,
   a weather forecasting supercomputer, Netflix.
9. Convert 42 to binary, octal, and hexadecimal by hand using repeated division,
   showing each step. Then verify your answers using Python's ``bin()``, ``oct()``,
   and ``hex()``.
10. Call ``to_base(42, b)`` for every base ``b`` from 2 to 16 and print the
    results. What do you notice as the base increases?
11. Write a ``from_base(s, base)`` function — the inverse of ``to_base`` — that
    converts a string representation back to a decimal integer. It should handle
    negative numbers (strings starting with ``-``) and bases up to 60. Test it
    by verifying that ``from_base(to_base(n, base), base) == n`` for several
    values of ``n`` and ``base``.
12. Use ``to_base`` to express 7,384 seconds in base 60. Then verify the result
    by computing the hours, minutes, and seconds manually
    (``7384 // 3600``, ``(7384 % 3600) // 60``, ``7384 % 60``).
    What familiar notation does the base-60 output resemble?
13. Write a Python loop that prints the complete truth table for OR and for XOR
    across all four input combinations. Then verify both of De Morgan's laws hold
    for every combination:

    .. code-block:: python

       for a in [False, True]:
           for b in [False, True]:
               assert not (a and b) == (not a or  not b)
               assert not (a or  b) == (not a and not b)

14. Implement ``nand(a, b)`` as ``not (a and b)``. Then express AND, OR, and NOT
    using *only* ``nand``:

    - ``NOT a``  is ``nand(a, a)``
    - ``a AND b`` is ``nand(nand(a, b), nand(a, b))``
    - ``a OR b``  is ``nand(nand(a, a), nand(b, b))``

    Verify each identity holds for all four input combinations. This property —
    that every logical operation can be built from NAND alone — is why real CPUs
    are constructed almost entirely from NAND gates.
15. Extend ``to_base`` to raise a ``ValueError`` with a descriptive message if
    ``base`` is less than 2 or greater than 60. Test that the error is raised
    correctly for ``base=1`` and ``base=61``.

.. rubric:: References

.. [DeanNorvig] Jeff Dean and Peter Norvig, *Latency Numbers Every Programmer
   Should Know*, Google, 2012.
   Widely circulated reference; canonical version maintained at
   https://gist.github.com/jboner/2841832

.. [HennessyPatterson2024] John L. Hennessy and David A. Patterson,
   *Computer Architecture: A Quantitative Approach*, 7th ed.,
   Morgan Kaufmann, 2024.
