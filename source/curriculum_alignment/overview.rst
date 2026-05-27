.. index::
   ACM-IEEE CS2013; curriculum alignment
   ACM-IEEE CS2023; curriculum alignment
   ACM; computing curriculum
   IEEE; computing curriculum
   curriculum; ACM/IEEE standards

.. _Curriculum-Alignment:

Alignment with ACM/IEEE Curriculum Standards
============================================

This chapter maps the content of *Introduction to Computer Science in Python*
against the two most widely used computing curriculum frameworks published by
the ACM and IEEE Computer Society:

- **CS2013** — *Computer Science Curricula 2013* (ACM/IEEE-CS Joint Task Force).
  The established reference used by the majority of accredited CS programmes.
  It organises content into **Knowledge Areas (KAs)**, each subdivided into
  **Knowledge Units (KUs)**, with topics rated Core Tier 1, Core Tier 2, or
  Elective.

- **CS2023** — *Computer Science Curricula 2023* (ACM/IEEE-CS, published
  December 2023).  The current revision; it retains the KA/KU structure but
  introduces a competency-based framework and revises the tier terminology
  to *Must* / *Should* / *May*.

.. warning::
   The CS2013 mappings in this chapter are authoritative. The CS2023 notes
   represent the authors' best understanding of a recently published document;
   instructors should verify CS2023 mappings against the official ACM/IEEE-CS
   publication before using them for formal accreditation purposes.

The CS Course Sequence
----------------------

.. index::
   CS0; Computing Principles
   CS1; Introduction to Computer Science
   CS2; Data Structures
   CS3; Algorithms
   CS1-CS8 course sequence
   numerical methods; curriculum history
   ACM/IEEE curriculum history
   course sequence; CS curriculum

The ACM/IEEE curriculum frameworks assume a standard undergraduate CS course
progression, but the naming of that progression has changed over time.

Historically, these labels were more extensive and more concrete than the
CS0-CS3 shorthand commonly used today. In the 1978 ACM curriculum, for
example, CS1 through CS8 denoted a sequence from programming through computer
systems, organization, data structures and algorithm analysis, and programming
language organization. Hemmendinger's historical review of the ACM and IEEE-CS
curriculum guidelines notes that earlier curriculum reports also gave
substantial attention to numerical computation: Curriculum 68 included
multiple numerical analysis courses, and Curriculum 78 retained advanced
numerical mathematics in analysis and linear algebra alongside advanced data
structures and algorithms (`author copy <https://cs.union.edu/~hemmendd/History/curric-hist.pdf>`__,
`CACM DOI <https://doi.org/10.1145/1230819.1230838>`__). In our view, some of
this breadth was muted over time as the discipline reconsidered which
mathematics belonged inside the CS curriculum and which belonged in supporting
mathematics courses. The persistence of advanced data structures, algorithm
analysis, and numerical methods in these historical designs is a useful
reminder that introductory programming was originally connected to a wider
mathematical and computational arc, not only to software construction.

Hemmendinger's summary of Curriculum 78 gives the following CS1-CS8 sequence:

.. list-table::
   :header-rows: 1
   :widths: 10 32 58

   * - Label
     - Curriculum 78 Topic
     - Historical Role
   * - **CS1**
     - Programming I
     - First programming course; beginning of the required CS core.
   * - **CS2**
     - Programming II
     - Continuation of programming, typically deepening control structures,
       modularity, and program design.
   * - **CS3**
     - Computer Systems
     - Introduction to systems concepts before the more focused organization
       and architecture courses.
   * - **CS4**
     - Computer Organization
     - Machine organization and the hardware/software boundary.
   * - **CS5**
     - File Processing
     - Application-oriented data storage and processing, reflecting the
       importance of files and records in computing practice.
   * - **CS6**
     - Operating Systems and Computer Architecture I
     - Systems-level continuation, joining operating systems with architecture.
   * - **CS7**
     - Data Structures and Algorithm Analysis
     - The advanced data structures and algorithms course in the intermediate
       core.
   * - **CS8**
     - Programming Language Organization
     - Programming-language concepts and organization, setting up later work
       in language theory and implementation.

Current ACM/IEEE curriculum guidelines no longer appear to organize the
undergraduate curriculum along the lines of a fixed CS1-CS8 course sequence.
This may be explained in part by the way some topics have been combined or
redistributed in modern practice. For example, material that once appeared
across CS3, CS4, and CS5 is often distributed across systems programming,
computer organization, data management, and operating systems courses today.

Modern ACM/IEEE guidelines instead describe knowledge areas, knowledge units,
outcomes, and competencies that departments may assemble into courses in
different ways. The rest of this chapter uses the more common contemporary
shorthand of CS0, CS1, CS2, CS3, and CS3+ only to indicate approximate course
level. The table below explains how those labels are used in this book; it is
not meant to replace the official ACM/IEEE knowledge-area structure.

.. list-table::
   :header-rows: 1
   :widths: 10 28 62

   * - Label
     - Common Course Title(s)
     - Focus
   * - **CS0**
     - Computing Principles;
       AP CS Principles;
       Introduction to Computing
     - Conceptual introduction to computing for non-majors or as a bridge
       course. Minimal or no programming; often uses block-based languages
       (Scratch), spreadsheets, or very simple Python/JavaScript scripts.
       Covers the societal impact of computing, the internet, data, and
       algorithms at a high level.
   * - **CS1**
     - Introduction to Computer Science;
       Introduction to Programming;
       Foundations of Computer Science
     - First programming course for majors. Variables, types, expressions,
       conditionals, loops, functions, basic I/O, and introductory data
       structures (lists, dictionaries). Typically taught in Python, Java,
       or C++. *This textbook targets CS1.*
   * - **CS2**
     - Data Structures;
       Data Structures and Algorithms;
       Object-Oriented Programming
     - Second programming course. Inheritance and polymorphism, linked
       lists, stacks, queues, trees, graphs, sorting algorithms, and
       introductory complexity analysis (Big-O). OOP design principles.
       Discrete Mathematics is often a co-requisite or prerequisite.
   * - **CS3**
     - Algorithms;
       Algorithm Design and Analysis;
       Systems Programming;
       Computer Organization
     - "CS3" is not a single course — it represents the tier of courses
       taken after CS2. Common CS3-level courses include: a formal
       *Algorithms* course (NP-completeness, dynamic programming,
       graph algorithms), *Systems Programming* (C, memory management,
       processes and threads), and *Computer Organization* (assembly
       language, caches, pipelines).
   * - **CS3+**
     - Compilers; Operating Systems;
       Programming Languages;
       Theory of Computation;
       Artificial Intelligence
     - Upper-division and graduate courses that build on a full CS1–CS3
       foundation. KUs at this level are not expected in an introductory
       curriculum.

How to Read the KA Tables
--------------------------

.. index:: curriculum alignment; coverage levels

Each Knowledge Area table below lists **every** Knowledge Unit in that area —
including units this textbook does not address. The **Coverage** column uses:

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Coverage
     - Meaning
   * - **Full**
     - All CS1-expected topics for this KU are substantively addressed.
   * - **Partial — CS1 gap**
     - This textbook covers part of the KU but is missing CS1-level
       content that *should* be added to a CS1 course.
   * - **Partial — CS2 gap**
     - The CS1-level content for this KU is complete. The remaining
       gaps are CS2+ topics that are intentionally deferred.
   * - **Minimal**
     - The topic is touched on incidentally but not developed to the
       depth the standard expects (used mainly for CS2-level KUs where
       the textbook happens to introduce the concept).
   * - **—**
     - Topic is absent from this textbook entirely.

The **Course Level** column shows where a KU is *first expected* in a typical
CS curriculum — CS0, CS1, CS2, CS3, or CS3+. For every row marked CS1,
the Coverage column explicitly flags whether further development is needed
in this book (CS1 gap) or whether the CS1 portion is already complete
(CS2 gap, or Full).

Coverage Summary
----------------

.. index:: curriculum alignment; summary

.. list-table::
   :header-rows: 1
   :widths: 34 10 8 8 8 14

   * - Knowledge Area
     - Total KUs
     - Full
     - Partial
     - Minimal
     - Not Covered
   * - SDF — Software Development Fundamentals
     - 4
     - 2
     - 2
     - 0
     - 0
   * - PL — Programming Languages
     - 10
     - 0
     - 3
     - 2
     - 5
   * - AL — Algorithms and Complexity
     - 7
     - 0
     - 1
     - 2
     - 4
   * - SP — Social Issues and Professional Practice
     - 9
     - 1
     - 1
     - 0
     - 7
   * - AR — Architecture and Organization
     - 8
     - 0
     - 0
     - 2
     - 6
   * - SE — Software Engineering
     - 10
     - 0
     - 4
     - 0
     - 6

Not-covered counts include both CS1-level gaps and CS2+/CS3+ topics that are
intentionally out of scope for a first course. The per-KA tables distinguish
these via the Course Level column.

Software Development Fundamentals (SDF)
----------------------------------------

.. index::
   ACM-IEEE CS2013; SDF
   ACM-IEEE CS2023; SDF
   SDF; Software Development Fundamentals

SDF is the Knowledge Area most directly targeted by a first programming course.
CS2013 assigns all four KUs to Core Tier 1 or Tier 1/2.  This textbook covers
SDF thoroughly — it is the backbone of the curriculum.

.. list-table::
   :header-rows: 1
   :widths: 26 10 8 36 20

   * - Knowledge Unit
     - CS2013 Tier
     - Level
     - Textbook Sections
     - Coverage
   * - **SDF1** Algorithms and Design
     - Tier 1
     - CS1
     - :doc:`Context </context/context>`,
       :doc:`Data </data/data>`,
       :doc:`Functions </functions/functions>`
     - **Full**
   * - **SDF2** Fundamental Programming Concepts
     - Tier 1
     - CS1
     - :doc:`Data </data/data>`,
       :doc:`Functions </functions/functions>`,
       :doc:`Decisions </decisions/decisions>`,
       :doc:`While Loops </while/while>`,
       :doc:`For Loops </for/for>`,
       :doc:`Files </files/files>`,
       :ref:`User Input <User-Input-Overview>`,
       :doc:`Recursion </recursion/recursion>`
     - **Full**
   * - **SDF3** Fundamental Data Structures
     - Tier 1/2
     - CS1
     - :doc:`Lists </lists/lists>`,
       :doc:`Tuples </tuples/tuples>`,
       :doc:`Dictionaries </dictionaries/dictionaries>`,
       :ref:`Lists of Dicts <Lists-Of-Dictionaries>`,
       :ref:`Dict Algorithms <Dictionary-Algorithms>`,
       :doc:`Data Structures </datastructures/datastructures>`.
       *Missing:* binary search trees, graphs
       (CS2 topics).
     - **Partial — CS2 gap**
   * - **SDF4** Development Methods
     - Tier 1
     - CS1
     - :doc:`Testing </testing/testing>`,
       :ref:`Error Handling <Error-Handling>`.
       *Missing:* systematic debugging strategies,
       refactoring as a standalone topic.
     - **Partial — CS1 gap**

.. index::
   SDF; Algorithms and Design
   SDF; Fundamental Programming Concepts
   SDF; Fundamental Data Structures
   SDF; Development Methods

**CS2023 note.** CS2023 retains all four SDF KUs and adds an explicit
competency requiring students to *select* the appropriate control structure
for a given problem — a distinction this textbook honours through its
separate :doc:`While Loops </while/while>` and :doc:`For Loops </for/for>`
chapters.

Programming Languages (PL)
---------------------------

.. index::
   ACM-IEEE CS2013; PL
   ACM-IEEE CS2023; PL
   PL; Programming Languages

CS2013 defines ten PL KUs. PL1 and PL4 are Core Tier 1 CS1 topics; PL2 and
PL3 become relevant by CS2. PL5–PL10 are CS2+/CS3+ and are not expected in
a first course. CS2023 reorganises and elevates type systems and functional
programming.

.. list-table::
   :header-rows: 1
   :widths: 26 10 8 36 20

   * - Knowledge Unit
     - CS2013 Tier
     - Level
     - Textbook Sections
     - Coverage
   * - **PL1** Object-Oriented Programming
     - Tier 1
     - CS1
     - :doc:`Classes </classes/classes>`.
       *Missing:* inheritance, subclasses,
       ``super()``, method overriding, polymorphism
       (basic inheritance is CS1; full polymorphism
       is CS2).
     - **Partial — CS1 gap**
   * - **PL2** Functional Programming
     - Tier 2
     - CS2
     - :ref:`List Comprehensions <List-Comprehensions>`,
       :ref:`Recursion Examples <Recursion-Examples>`
       (memoisation via ``lru_cache``).
       *Missing:* closures, ``map``/``filter``,
       higher-order functions as a paradigm.
     - **Minimal**
   * - **PL3** Event-Driven and Reactive Programming
     - Tier 2
     - CS1
     - :ref:`Terminal User Interfaces <Terminal-User-Interfaces>`
       (Textual event loop, button events,
       widget updates).
       *Missing:* reactive/stream programming models
       (CS2 topic).
     - **Partial — CS2 gap**
   * - **PL4** Basic Type Systems
     - Tier 1
     - CS1
     - :doc:`Data </data/data>`,
       :ref:`Type Hints <Type-Hints-Functions>`.
       *Missing:* formal type compatibility rules,
       type inference (CS2 topics).
     - **Partial — CS2 gap**
   * - **PL5** Program Representation
     - Tier 2
     - CS2
     - (CS2 topic — not addressed)
     - **—**
   * - **PL6** Language Translation and Execution
     - Tier 2
     - CS2
     - :ref:`Modules <Modules-And-Variable-Scope>`
       (``__name__``, interpreter model).
       Superficial; bytecode and runtime model absent.
     - **Minimal**
   * - **PL7** Syntax Analysis
     - Tier 2
     - CS3
     - (CS3 topic — not addressed)
     - **—**
   * - **PL8** Semantics
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**
   * - **PL9** Pragmatics
     - Tier 2
     - CS2
     - (CS2 topic — not addressed)
     - **—**
   * - **PL10** Logic Programming
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**

.. index::
   PL; Object-Oriented Programming
   PL; Functional Programming
   PL; Event-Driven Programming
   PL; Basic Type Systems
   PL; Language Translation and Execution

**CS2023 note.** CS2023 elevates PL2/Functional Programming from Tier 2 to
*Should*, reflecting the industry shift toward functional styles in Python,
JavaScript, and Rust. It also introduces a dedicated *Type Systems and
Semantics* KU aligned with Python's gradual-typing model; the
:ref:`Type Hints <Type-Hints-Functions>` coverage could be deepened to meet
this expectation. Inheritance and polymorphism remain *Must*-level; their
absence is the largest single PL gap.

Algorithms and Complexity (AL)
-------------------------------

.. index::
   ACM-IEEE CS2013; AL
   ACM-IEEE CS2023; AL
   AL; Algorithms and Complexity

CS2013 has seven AL KUs. AL1–AL3 are Core Tier 1 but are primarily taught in
CS2 (Data Structures), where formal analysis, sorting theory, and tree/graph
algorithms are the main subject. AL4–AL7 are Tier 2 or Elective and belong
to a dedicated CS3-level Algorithms course.

.. list-table::
   :header-rows: 1
   :widths: 26 10 8 36 20

   * - Knowledge Unit
     - CS2013 Tier
     - Level
     - Textbook Sections
     - Coverage
   * - **AL1** Basic Analysis
     - Tier 1
     - CS2
     - :doc:`Lists </lists/lists>`,
       :doc:`Data Structures </datastructures/datastructures>`
       (informal Big-O comparisons).
       *Missing:* formal asymptotic notation,
       recurrence relations, space/time trade-offs.
     - **Minimal**
   * - **AL2** Algorithmic Strategies
     - Tier 1
     - CS2
     - :doc:`Recursion </recursion/recursion>`
       (divide-and-conquer).
       *Missing:* greedy algorithms, explicit dynamic
       programming, backtracking.
     - **Minimal**
   * - **AL3** Fundamental Data Structures and Algorithms
     - Tier 1
     - CS2
     - :ref:`Sorting <Sorting>`,
       :ref:`Searching <Searching>`,
       :doc:`Dictionaries </dictionaries/dictionaries>`
       (hash tables, conceptual),
       :doc:`Data Structures </datastructures/datastructures>`
       (stacks, queues, linked lists).
       *Missing:* binary search trees, graph
       algorithms (BFS, DFS) — CS2 topics.
     - **Partial — CS2 gap**
   * - **AL4** Basic Computability Theory
     - Tier 2
     - CS3
     - (CS3 topic — not addressed)
     - **—**
   * - **AL5** The Complexity Classes P and NP
     - Tier 2
     - CS3
     - (CS3 topic — not addressed)
     - **—**
   * - **AL6** Automata Theory
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**
   * - **AL7** Advanced Computational Complexity
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**

.. index::
   AL; Basic Analysis
   AL; Algorithmic Strategies
   AL; Fundamental Data Structures and Algorithms

**CS2023 note.** CS2023 retains AL1–AL3 at *Must* level and adds stronger
guidance on analysing recursive algorithms via recurrence relations. The
:doc:`Recursion </recursion/recursion>` chapter provides the right examples
but does not derive the corresponding complexity expressions.

Social Issues and Professional Practice (SP)
--------------------------------------------

.. index::
   ACM-IEEE CS2013; SP
   ACM-IEEE CS2023; SP
   SP; Social Issues and Professional Practice

CS2013 has nine SP KUs. SP1–SP3 (Social Context, Analytical Tools, and
Professional Ethics) are Core Tier 1 and are expected in every CS programme
including CS1. SP4–SP6 are Tier 2, appropriate for CS1 but often deferred to
CS2. SP7, SP8, and SP9 are Elective; SP8 (History) is addressed in full.

.. list-table::
   :header-rows: 1
   :widths: 26 10 8 36 20

   * - Knowledge Unit
     - CS2013 Tier
     - Level
     - Textbook Sections
     - Coverage
   * - **SP1** Social Context
     - Tier 1
     - CS1
     - :doc:`Context </context/context>`
       (motivational framing of computing's societal
       role). *Missing:* structured analysis of
       computing's impact on employment, culture,
       and underrepresented communities.
     - **Partial — CS1 gap**
   * - **SP2** Analytical Tools
     - Tier 1
     - CS1
     - (Not addressed — ethical reasoning frameworks
       such as consequentialism and deontology are
       not covered. **CS1 content to be added.**)
     - **—**
   * - **SP3** Professional Ethics
     - Tier 1/2
     - CS1
     - (Not addressed — ACM Code of Ethics, academic
       integrity, computing law not covered.
       **CS1 content to be added.**)
     - **—**
   * - **SP4** Intellectual Property
     - Tier 2
     - CS1
     - (Not addressed — copyright, open-source
       licensing not covered.
       **CS1 content to be added.**)
     - **—**
   * - **SP5** Privacy and Civil Liberties
     - Tier 2
     - CS1
     - (Not addressed — data privacy, surveillance,
       encryption policy not covered.
       **CS1 content to be added.**)
     - **—**
   * - **SP6** Professional Communication
     - Tier 2
     - CS2
     - (CS2 topic — technical writing and oral
       presentations not addressed)
     - **—**
   * - **SP7** Sustainability
     - Elective
     - CS2
     - (CS2 topic — not addressed)
     - **—**
   * - **SP8** History
     - Elective
     - CS1
     - :ref:`Computing History <Computing-History>`
       (prehistory through stored-program era; key
       figures including women ENIAC programmers
       and Ada Lovelace).
     - **Full**
   * - **SP9** Economics of Computing
     - Elective
     - CS2
     - (CS2 topic — not addressed)
     - **—**

.. index::
   SP; Social Context
   SP; Analytical Tools
   SP; Professional Ethics
   SP; Intellectual Property
   SP; Privacy and Civil Liberties
   SP; History
   ACM Code of Ethics; not covered

**CS2023 note.** CS2023 makes Professional Ethics a *Must* topic and expands
it to include AI ethics, algorithmic bias, and data privacy. It also adds a
new *Diversity, Equity, and Inclusion* KU. The
:ref:`Computing History <Computing-History>` chapter partially addresses DEI
history through the ENIAC programmers and Ada Lovelace, but a systematic
treatment is needed.

Architecture and Organization (AR)
------------------------------------

.. index::
   ACM-IEEE CS2013; AR
   ACM-IEEE CS2023; AR
   AR; Architecture and Organization

CS2013 has eight AR KUs. AR1 and AR2 are Core Tier 1 and expected at a
conceptual level in CS1; AR3 (Assembly Level) is Tier 1 but is the primary
subject of a CS2/CS3-level Computer Organization course. AR4–AR8 are Tier 2
or Elective and belong to upper-division systems courses.

.. list-table::
   :header-rows: 1
   :widths: 26 10 8 36 20

   * - Knowledge Unit
     - CS2013 Tier
     - Level
     - Textbook Sections
     - Coverage
   * - **AR1** Digital Logic and Digital Systems
     - Tier 1
     - CS2
     - :ref:`Hardware <Hardware-And-Software>`
       (CPU, RAM, storage overview),
       :ref:`Computing History <Computing-History>`
       (von Neumann architecture).
       *Missing:* Boolean gates, combinational
       circuits, fetch-decode-execute cycle in detail.
     - **Minimal**
   * - **AR2** Machine Level Representation of Data
     - Tier 1
     - CS2
     - :ref:`f-strings <fstrings>`
       (hex/binary format specifiers),
       :ref:`Computing History <Computing-History>`
       (Pascaline, two's complement mentioned
       historically).
       *Missing:* signed/unsigned integers, IEEE 754
       floating point, two's complement arithmetic.
     - **Minimal**
   * - **AR3** Assembly Level Machine Organization
     - Tier 1
     - CS2
     - (CS2/Systems topic — not addressed)
     - **—**
   * - **AR4** Memory System Organization and Architecture
     - Tier 2
     - CS3
     - (CS3 topic — not addressed)
     - **—**
   * - **AR5** Interfacing and Communication
     - Tier 2
     - CS3
     - (CS3 topic — not addressed)
     - **—**
   * - **AR6** Functional Organization
     - Tier 2
     - CS3
     - (CS3 topic — not addressed)
     - **—**
   * - **AR7** Multiprocessing and Alternative Architectures
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**
   * - **AR8** Performance Enhancements
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**

.. index::
   AR; Digital Logic and Digital Systems
   AR; Machine Level Representation of Data
   AR; Assembly Level Machine Organization

**CS2023 note.** CS2023 retains AR1 and AR2 at *Must* level but clarifies
that a CS1 course need only achieve a *conceptual* treatment of hardware
organisation — gate-level circuits and assembly language remain CS2
expectations.

Software Engineering (SE)
--------------------------

.. index::
   ACM-IEEE CS2013; SE
   ACM-IEEE CS2023; SE
   SE; Software Engineering

CS2013 has ten SE KUs. SE3 (Tools and Environments) is Core Tier 1 and the
only SE KU expected at CS1. SE1, SE6, and SE7 bridge CS1 and CS2; the
remaining six KUs (SE2, SE4, SE5, SE8–SE10) belong to CS2+ software
engineering courses.

.. list-table::
   :header-rows: 1
   :widths: 26 10 8 36 20

   * - Knowledge Unit
     - CS2013 Tier
     - Level
     - Textbook Sections
     - Coverage
   * - **SE1** Software Processes
     - Tier 2
     - CS2
     - :doc:`Testing </testing/testing>`
       (test-first development),
       :doc:`Basic String Ops </basicstringops/basicstringops>`
       (problem-solving framework).
       *Missing:* SDLC models, agile methods,
       iterative development as a formal process
       (CS2 topics).
     - **Partial — CS2 gap**
   * - **SE2** Project Management
     - Tier 2
     - CS2
     - (CS2 topic — not addressed)
     - **—**
   * - **SE3** Tools and Environments
     - Tier 1
     - CS1
     - :ref:`Terminal <Terminal-Overview>`
       (CLI, shell commands, redirection),
       :doc:`Testing </testing/testing>` (pytest),
       :ref:`User Input <User-Input-Overview>`
       (``sys.argv``).
       *Missing:* version control (lab stub exists
       but content not yet written).
     - **Partial — CS1 gap**
   * - **SE4** Requirements Engineering
     - Tier 2
     - CS2
     - (CS2 topic — not addressed)
     - **—**
   * - **SE5** Software Design
     - Tier 2
     - CS2
     - (CS2 topic — not addressed)
     - **—**
   * - **SE6** Software Construction
     - Tier 2
     - CS1
     - :ref:`Writing Tests <Writing-Tests>`
       (docstrings, type hints, code style).
       *Missing:* code review, pair programming,
       static analysis tools (CS2 topics).
     - **Partial — CS2 gap**
   * - **SE7** Verification and Validation
     - Tier 2
     - CS1
     - :ref:`Pytest Intro <Pytest-Intro>`,
       :ref:`Writing Tests <Writing-Tests>`
       (unit tests, assert statements, coverage
       concept). *Missing:* integration testing,
       regression testing, formal V&V (CS2 topics).
     - **Partial — CS2 gap**
   * - **SE8** Software Evolution
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**
   * - **SE9** Software Reliability
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**
   * - **SE10** Formal Methods
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**

.. index::
   SE; Software Processes
   SE; Tools and Environments
   SE; Software Construction
   SE; Verification and Validation
   version control; not covered

**CS2023 note.** CS2023 promotes version control (Git) to *Must* at the
introductory level, elevating it from a Tier 2 detail to an expected CS1
competency. The existing appendix stub ``lab-versioncontrol.rst`` would, once
completed, close this gap.

Gap Analysis
------------

.. index:: curriculum alignment; gap analysis, curriculum; gaps

The table below consolidates every KU rated **Minimal** or **—** that falls
within the CS1 course level. CS2/CS3/CS3+ topics are intentionally deferred
and are not listed as gaps for a CS1 textbook.

.. list-table::
   :header-rows: 1
   :widths: 20 8 8 34 30

   * - Gap
     - KU
     - Priority
     - What Is Missing
     - Suggested Remedy
   * - Professional ethics
     - SP3
     - **High**
     - ACM Code of Ethics; academic integrity;
       computing law; AI ethics and algorithmic
       bias (CS2023 adds these).
     - Add a dedicated section to
       :doc:`Context </context/context>` or a short
       standalone chapter.
   * - Ethical reasoning tools
     - SP2
     - **High**
     - Philosophical frameworks (consequentialism,
       deontology, virtue ethics) for evaluating
       computing decisions.
     - Combine with the SP3 remediation above.
   * - Inheritance and polymorphism
     - PL1
     - **High**
     - Subclasses, ``super()``, method overriding,
       duck typing as Python's polymorphism model.
     - Extend :doc:`Classes </classes/classes>`
       with a second section on inheritance.
   * - Intellectual property
     - SP4
     - Medium
     - Copyright, open-source licensing (MIT, GPL,
       Apache), software patents.
     - Add a short section to
       :doc:`Context </context/context>` or
       :ref:`Modules <Modules-And-Variable-Scope>`
       (e.g., choosing a licence for your project).
   * - Privacy and civil liberties
     - SP5
     - Medium
     - Data collection, surveillance, encryption
       policy, GDPR concepts.
     - Add an ethical reflection to
       :ref:`Internet Data <Internet-Data>` after
       the API usage sections.
   * - Version control
     - SE3
     - Medium
     - Git workflow; commits; branches;
       pull requests; ``git log`` / ``git blame``.
     - Complete ``appendix/lab-versioncontrol.rst``.
   * - Event-driven depth
     - PL3
     - Low
     - Reactive/stream programming models beyond
       simple widget callbacks.
     - Extend the
       :ref:`Terminal User Interfaces <Terminal-User-Interfaces>`
       chapter; appropriate for CS1 enrichment.

Notes on CS2023
---------------

.. index:: CS2023; differences from CS2013, CS2023; competency framework

CS2023 represents an evolution rather than a revolution of CS2013. The
following changes are most relevant to this textbook:

**Competency-based framing.** CS2023 defines *competencies* (knowledge +
skills + dispositions) alongside traditional topic lists. A competency for
SDF2/Fundamental Programming Concepts, for example, requires students not
just to understand loops but to *select the appropriate loop construct* for a
given problem — a distinction this textbook honours through its explicit
:doc:`While Loops </while/while>` vs. :doc:`For Loops </for/for>` chapters.

**Professional Ethics elevated.** Ethics moved from Tier 1/Elective in CS2013
to *Must* in CS2023 across SP2 and SP3. The gap identified above is more
urgent under CS2023.

**Functional programming elevated.** CS2023 raises PL2/Functional Programming
from Tier 2 to *Should* — one level below *Must* — reflecting the industry
trend toward functional styles in Python, JavaScript, and Rust. The
:ref:`List Comprehensions <List-Comprehensions>` section is a good foundation
to build on.

**Type systems expanded.** CS2023 introduces a dedicated *Type Systems and
Semantics* KU (building on PL4) that includes gradual typing — highly relevant
to Python's ``typing`` module and the :ref:`Type Hints <Type-Hints-Functions>`
approach taken throughout this textbook. Deepening that coverage would meet
this expectation.

**Version control promoted.** CS2023 elevates SE3/Version Control to *Must*
at the CS1 level, reflecting industry consensus that Git is a day-one skill.

**New: Diversity, Equity, and Inclusion.** CS2023 adds a KU requiring
programmes to address DEI in computing contexts. The
:ref:`Computing History <Computing-History>` chapter partially addresses this
through its coverage of the ENIAC programmers and Ada Lovelace, but a more
systematic treatment is needed.

Recommendations for Instructors
---------------------------------

.. index:: curriculum alignment; instructor recommendations

This textbook is designed as a CS1 course and intentionally defers some
topics (formal algorithm analysis, trees and graphs, assembly language,
compilers) to CS2 and later courses. The following additions would bring it
to near-full CS2013 Core Tier 1 coverage for a CS1 context:

1. **Add an ethics section** (closes SP2 + SP3) to
   :doc:`Context </context/context>` covering the ACM Code of Ethics,
   ethical reasoning frameworks, academic integrity, and basic computing law.
   This is the highest-priority gap under both CS2013 and CS2023.

2. **Add an inheritance section** (closes PL1) to
   :doc:`Classes </classes/classes>` demonstrating subclasses, ``super()``,
   and method overriding with a concrete example (e.g., extending the
   ``Contact`` class to ``ProfessionalContact``).

3. **Complete the version control lab** (closes SE3) in
   ``appendix/lab-versioncontrol.rst`` covering Git commits, branches, and
   the pull-request workflow. This is *Must*-level in CS2023.

4. **Weave privacy and IP notes** (partially closes SP4 + SP5) into
   :ref:`Internet Data <Internet-Data>` when discussing API keys, rate
   limits, and data collected from users.

Topics such as formal Big-O proofs, binary search trees, greedy algorithms,
and machine-level data representation are better addressed in CS2 (Data
Structures). Topics such as Boolean gates, assembly language, and the
fetch-decode-execute cycle belong in a CS2/CS3-level Computer Organization
course. This textbook lays the groundwork for all of them through its
coverage of :doc:`Recursion </recursion/recursion>`,
:doc:`Data Structures </datastructures/datastructures>`,
and the :ref:`Hardware <Hardware-And-Software>` and
:ref:`Computing History <Computing-History>` chapters.
