# AGENTS.md — Introduction to Computer Science in Python

This file gives AI agents and contributors a complete picture of the project:
what it is, where things stand, and how to work on it effectively.

---

## What this project is

**Introduction to Computer Science in Python: Principles and Practice** is a
Sphinx-based course textbook for Comp 170 (Introduction to Computer Science) at
Loyola University Chicago.  It is authored by the Computer Science Department
Faculty at Loyola University Chicago.

The book teaches introductory CS concepts using Python.  It is a ground-up
Python rewrite of the prior C# edition (`introcs-csharp`, located at
`~/Work/introcs-csharp`).  Chapter structure and pedagogical arc are preserved;
all code and language-specific explanations are Python-native.

The book's broader argument — that programming, data structures, and algorithms
should be taught as foundations for systems and engineering thinking, especially
in the age of AI — is articulated in:

> Chandra N. Sekharan and George K. Thiruvathukal,
> *"Now's the Time: Computer Science Must Evolve to Emphasize Software and
> Systems Engineering with Artificial Intelligence (AI),"*
> IEEE Computer, Education Department, 2026.
> https://arxiv.org/abs/2604.27230

---

## Authorship and AI assistance

The intellectual content of this book — its argument, structure, pedagogy,
examples, and prose — originated with George K. Thiruvathukal's own work on the
book content, building on the prior C# edition and the source materials listed
below. The ideas and editorial direction are the author's; AI tools are used
only to assist with drafting, translation, editing, and tooling under that
direction.

Both **Anthropic's Claude** and **OpenAI's models** are used as assistants in
this project (for example, adapting C# material to Python, expanding outlines
into prose, and maintaining the Sphinx build). All AI-assisted output is
reviewed and revised by the author; the AI does not set the book's intellectual
agenda.

---

## Remote repository

```
git@github.com:LoyolaChicagoBooks/introcs-python-ai.git
```

Branch: `main`

Latest release tag: `v0.1`

---

## Deployed sites

- **GitHub Pages (custom domain):** https://introcs-python.cs.luc.edu
- **CNAME file:** generated at CI time (`build/html/CNAME`) — do not commit it
- **GitHub Releases (PDF + EPUB):** published automatically on tag pushes

---

## Source material

When adapting or adding content, draw from:

1. **`~/Work/introcs-csharp`** — the C# predecessor; primary source for
   chapter structure, example programs, and narrative voice.
2. **`~/Work/SE4ML`** — secondary source for systems/AI framing.
3. **`~/Work/comp-501-book`** — PhD student contributions (COMP 501, Loyola);
   source for: hardware/software, terminal, modules/scope, user input, error
   handling, lists of dicts, dict algorithms, internet data, GUI chapters.
4. **`~/Work/operatingsystems`** — Linux terminal examples drawn from
   `source/introduction.rst`.

Every RST file contributed by PhD students carries a `.. note::` attribution:
`*Source:* Contributed by PhD students in COMP 501 at Loyola University Chicago.`

---

## Content status (as of 2026-05-11)

### Complete chapters (full prose, no stubs)

| Chapter | Directory |
|---------|-----------|
| Context (motivation, CS intro) | `source/context/` |
| **Episodes in Computing History** *(preliminary)* | `source/computing_history/` |
| Hardware and Software | `source/hardware/` |
| The Terminal | `source/terminal/` |
| Data (variables, arithmetic, I/O, types) | `source/data/` |
| Functions | `source/functions/` |
| Modules and Variable Scope | `source/modules/` |
| Basic String Operations | `source/basicstringops/` |
| Decisions | `source/decisions/` |
| User Input | `source/user_input/` |
| While Loops | `source/while/` |
| For Loops | `source/for/` |
| Files & pathlib | `source/files/` |
| Error Handling | `source/error_handling/` |
| Lists | `source/lists/` |
| Tuples | `source/tuples/` |
| Dictionaries | `source/dictionaries/` |
| Lists of Dictionaries | `source/lists_of_dicts/` |
| Dictionary Algorithms | `source/dict_algorithms/` |
| Internet Data | `source/internet_data/` |
| Simulation | `source/simulation/` |
| Classes & dataclasses | `source/classes/` |
| Testing (pytest) | `source/testing/` |
| Recursion | `source/recursion/` |
| Data Structures | `source/datastructures/` |
| Terminal User Interfaces (Rich/Textual) | `source/ui/` |
| Case Studies | `source/case_studies/` |
| Interactive Python in the Browser (JupyterLite/Pyodide) | `source/interactive/` |

### Stub chapters (outlined, ready to write)

| Chapter | Directory | Notes |
|---------|-----------|-------|
| Linear Algebra | `source/linear_algebra/` | Four files with detailed `.. todo::` outlines: `overview.rst`, `vectors.rst`, `matrices.rst`, `applications.rst`. Placed in toctree after Lists, before Tuples. |

### Appendix

| File | Status |
|------|--------|
| `lesson_plan.rst` | Complete — 16-week table with chapter links |
| `contributors.rst` | Complete — all authors, faculty, emeritus |
| `acknowledgments.rst` | Stub |
| `cmdline.rst` | Stub |
| `precedence.rst` | Stub |
| `lab-versioncontrol.rst` | Stub |
| `homework-gradecalculation.rst` | Stub |

---

## Repository layout

```
introcs-python/
├── AGENTS.md                   # this file
├── Makefile                    # Sphinx build targets
├── requirements.txt            # sphinx, sphinx-book-theme, etc.
├── .github/workflows/main.yml  # CI: HTML → GitHub Pages; PDF/EPUB → releases
└── source/
    ├── conf.py                 # Sphinx configuration
    ├── index.rst               # Top-level toctree
    ├── _static/logo.png        # Book logo
    ├── context/                # Ch 1 — motivation
    ├── computing_history/      # Ch 2 — episodes in computing history (preliminary)
    ├── hardware/               # Ch 3
    ├── terminal/               # Ch 4
    ├── data/                   # Ch 5
    ├── functions/              # Ch 6
    ├── modules/                # Ch 7
    ├── basicstringops/         # Ch 8
    ├── decisions/              # Ch 9
    ├── user_input/             # Ch 10
    ├── while/                  # Ch 11
    ├── for/                    # Ch 12
    ├── files/                  # Ch 13
    ├── error_handling/         # Ch 14
    ├── lists/                  # Ch 15
    ├── tuples/                 # Ch 16
    ├── dictionaries/           # Ch 17
    ├── lists_of_dicts/         # Ch 18
    ├── dict_algorithms/        # Ch 19
    ├── internet_data/          # Ch 20
    ├── classes/                # Ch 21
    ├── testing/                # Ch 22
    ├── recursion/              # Ch 23
    ├── datastructures/         # Ch 24
    ├── gui/                    # Ch 25
    ├── linear_algebra/         # Ch 16 (stub) — overview, vectors, matrices, applications
    ├── simulation/             # Ch 22 — Monte Carlo
    ├── case_studies/           # Ch 27 — Monte Carlo, Chicago 311 graffiti
    └── appendix/               # lesson_plan, contributors, stubs
```

Each chapter follows the two-file pattern:
- `chapter/chapter.rst` — container: `#`-underlined title + toctree
- `chapter/overview.rst` (or multiple sub-files) — content: `=`-underlined title

---

## Build instructions

```bash
# Install dependencies (once) — always use the project .venv
.venv/bin/pip install -r requirements.txt

# HTML (fast, for day-to-day work) — use .venv sphinx-build, not make
.venv/bin/sphinx-build -b html source build/html
open build/html/index.html

# Full clean rebuild (required when adding new toctree entries)
rm -rf build/ && .venv/bin/sphinx-build -b html source build/html

# Check for Sphinx warnings/errors
.venv/bin/sphinx-build -b html source build/html 2>&1 | grep -E "ERROR|WARNING"

# PDF (requires TeX Live full install with xelatex)
make latex
# then compile PDF:
make -C build/latex
open build/latex/introcs-python.pdf

# EPUB
make epub
```

The PDF uses **xelatex** (not pdflatex) because the book contains Unicode
characters throughout. The `texlive-full` CI image already includes all
required fonts — no `tlmgr install` step is needed.

### JupyterLite (interactive chapter)

The `source/interactive/` chapter embeds live, in-browser Python REPLs with the
`.. replite::` directive from **jupyterlite-sphinx** (Pyodide/WebAssembly). This
means:

- `jupyterlite-sphinx` and `jupyterlite-pyodide-kernel` are required and are
  listed in `requirements.txt`. `conf.py` enables the `jupyterlite_sphinx`
  extension; a clean `pip install -r requirements.txt` is needed for the build.
- Every HTML build runs an embedded JupyterLite build (visible as
  `[jupyterlite-sphinx] Running JupyterLite build`) and generates
  `source/.jupyterlite.doit.db` and `source/_contents/` — both are build
  artifacts and are **gitignored**; do not commit them.
- The REPLs need to be served over HTTP to work — open the built page through a
  local server (`python -m http.server` from `build/html`), not via `file://`,
  or the Pyodide/WebAssembly fetches fail. numpy and matplotlib run inside the
  browser via Pyodide, so they do not need to be in `requirements.txt`.

#### Runnable snippets in regular chapters (``.. try_examples::``)

Beyond the dedicated `source/interactive/` chapter (which uses ``.. replite::``
REPL widgets), individual short examples throughout the book are made runnable
with the **``.. try_examples::``** directive from jupyterlite-sphinx. It renders
the code in every format and adds a **"Try it live ▶"** button (HTML only) that
swaps the code for a live, editable JupyterLite cell. This is the standard
mechanism for in-text runnable snippets; prefer it over ``.. replite::`` outside
the interactive chapter.

The feature is introduced to readers early, in
`source/context/intro.rst` (the "Running Code in Your Browser" section, label
``try-it-live``) — a short explanation plus a live hello/``datetime.now()``
demo, well before the first toggle appears in `data/`. The first toggle in
`data/arithmetic.rst` links back to that section. The dedicated
`source/interactive/` chapter (label ``Interactive-Python-Overview``) remains
the deep-dive.

Conventions:

- **The directive content must be doctest format** (``>>>`` statements, ``...``
  continuation lines, then expected output with no prompt). A multiline suite
  ends with a bare ``...`` line before its output. The rendered code therefore
  shows in REPL style — convert script-style examples accordingly.
- **Replace, do not duplicate.** The ``try_examples`` block *is* the example;
  remove the original ``.. code-block::`` (and any separate "Output:" block) so
  the code is not shown twice. The code still appears in PDF/EPUB because the
  directive renders its content in all formats; only the button is HTML.
- **Each cell must be self-contained** — fold in any function/variable
  definition the snippet depends on, since every ``try_examples`` block gets its
  own kernel.
- **Outputs are shown to readers** — run the snippet with `.venv/bin/python` and
  paste the exact output. For ``random`` examples, seed with `random.seed(0)` so
  the displayed output is reproducible.
- **Skip non-runnable examples**: `input()`, file I/O, networking, `subprocess`,
  `literalinclude` multi-file programs, intentionally-incomplete fragments, and
  anything whose output contains a blank line (doctest needs `<BLANKLINE>`,
  which renders literally — keep those as a static `.. code-block::`).
- Standard option: ``:height:`` ~220–340px. No ``.. only::`` wrapper is needed.
- **Config (`conf.py`):** `try_examples_global_button_text` and
  `try_examples_global_warning_text` set the button label and the in-notebook
  warning. (`global_enable_try_examples` is **not** used — it only processes
  Python docstrings via autodoc, not hand-written ``.rst``, so every runnable
  example needs its own explicit directive.)
- **EPUB:** the run button is raw HTML and the EPUB builder's format is also
  ``html``, so it would otherwise appear (dead) in the EPUB. `source/_static/
  epub-overrides.css` (wired via `epub_css_files`) hides it; the LaTeX/PDF build
  drops raw HTML automatically.

Coverage is **complete** across all chapters with self-contained Python
(~216 ``try_examples`` in ~49 files): `data`, `functions`, `basicstringops`,
`decisions`, `while`, `for`, `modules`, `lists`, `tuples`, `dictionaries`,
`lists_of_dicts`, `dict_algorithms`, `simulation`, `classes`, `recursion`,
`datastructures`, `error_handling`. The interim ``.. replite::`` widgets have all
been converted; ``.. replite::`` now appears only in the dedicated
`source/interactive/` chapter.

Chapters intentionally left without ``try_examples`` (nothing self-contained to
run): `user_input`, `internet_data` (network), `testing` (needs a pytest
runner), `terminal`/`hardware`/`context`/`computing_history` (prose/shell), and
the `linear_algebra` stub — add numpy vector/matrix examples there once it is
written.

To validate output accuracy after editing, extract each ``try_examples`` block
and run it through ``python -m doctest`` (try_examples does **not** execute
doctests at build time, so wrong output is not caught by the Sphinx build). Watch
for two non-failures: a trailing space after ``print(..., end=" ")`` loops, and
tab vs. space rendering — both display fine. A genuine failure is any output
containing a blank line (keep those examples static).

---

## GitHub Actions CI

`.github/workflows/main.yml`:

- **Every push to `main`**: builds HTML, LaTeX, EPUB; compiles PDF with
  `xu-cheng/texlive-action/full`; deploys HTML to GitHub Pages at
  `https://introcs-python.cs.luc.edu`.
- **Tag push (`v*`)**: publishes `introcs-python.pdf` and `introcs-python.epub`
  as GitHub Release assets via `softprops/action-gh-release`.
- **`workflow_dispatch`**: manual trigger from the Actions tab.

Do **not** add `tlmgr install` steps — the full TeXLive image already contains
everything needed, and network-dependent `tlmgr` calls have failed in CI.

---

## RST writing conventions

### File structure

Every content file must follow this pattern:

```rst
.. index:: keyword, another keyword

.. _Label-Name:

Section Title
=============

.. note::

   *Source:* Adapted from the C# edition (``chapter/file.rst``).
   <what changed for Python>

[prose]

.. code-block:: python

   [example]

Output:

.. code-block:: none

   [output]
```

### Heading levels

| Level | Underline char | Used for |
|-------|---------------|----------|
| 1 | `#` (no overline) | Chapter container title (`chapter.rst`) |
| 2 | `=` | Section title (top of each content `.rst` file) |
| 3 | `-` | Subsection |
| 4 | `^` | Sub-subsection |

### Code blocks

- `.. code-block:: python` — short Python fragments, syntax examples,
  intentionally incomplete code, review questions, labs, and exercises
- `.. literalinclude::` — longer runnable examples from
  `examples/introcs-python/<chapter>/`; use excerpt markers such as
  `# start: name` / `# end: name` when a section shows one part of a larger file
- `.. code-block:: none` — output, shell commands, syntax diagrams
- `.. code-block:: bash` — shell/Linux commands
- Always precede output blocks with a plain `Output:` line (not a directive)

### Review questions

Each numbered review question must contain **exactly one question**.  If a
topic naturally has two parts, use `a.` / `b.` / `c.` sub-items:

```rst
#.  Main question stem.

    a.  Part one.
    b.  Part two.
```

### Voice and tone

- Direct, instructional, patient — follow the C# edition's style
- Explain the *why*, not just the *what*
- Second person ("you", "your program")
- Bold (`**term**`) for key terms when first introduced in characteristics lists
- Prefer prose paragraphs over bullet lists
- Soften absolute statements: prefer "is unlikely to" over "cannot"

---

## Python idioms to prefer

- f-strings over `%` or `.format()`
- `pathlib.Path` over `os.path`
- `with open(...) as f:` for all file I/O
- `for item in iterable:` over index-based loops where natural
- `snake_case` for variables/functions, `PascalCase` for classes
- Raise `ValueError` for invalid arguments (not silent failure)
- **pandas** for all tabular/CSV data work — `pd.read_csv`, `df.to_csv(index=False)`,
  boolean indexing, `value_counts()`, `groupby()`.  Do not use `csv.DictReader`/
  `csv.DictWriter` or `collections.Counter` for tasks pandas handles naturally.

---

## C# → Python translation reference

| C# | Python |
|----|--------|
| `Console.WriteLine(x)` | `print(x)` |
| `Console.Write(x)` | `print(x, end='')` |
| `Console.ReadLine()` | `input()` |
| `int.Parse(s)` / `double.Parse(s)` | `int(s)` / `float(s)` |
| `{0:F2}` format strings | f-string `{value:.2f}` |
| `//` comments | `#` comments |
| `&&`, `\|\|`, `!` | `and`, `or`, `not` |
| `else if` | `elif` |
| `foreach (var x in seq)` | `for x in seq:` |
| `List<T>` | `list` |
| `Dictionary<K,V>` | `dict` |
| `Stack<T>` | `list` (append/pop) |
| `Queue<T>` | `collections.deque` |
| NUnit `[Test]` / `Assert.AreEqual` | pytest `def test_*` / `assert` |
| `null` | `None` |

---

## Key content notes

### Computing history chapter (`source/computing_history/`)

Preliminary — not intended to be exhaustive. Based primarily on the author's
own published works:
- "Episodes in Computing History — Salon Talk" (Thiruvathukal, 2025)
- "Computer Science and Cultural History: A Dialogue" (Thiruvathukal & Dennis, CESTEMER 2017)
- "AI &| ML" panel talk (Thiruvathukal, LUCRA 2024)
- CiSE Editor-in-Chief mini-history project (2013–2016)

### Terminal chapter (`source/terminal/`)

Extended with Linux command examples drawn from `~/Work/operatingsystems/source/introduction.rst`.
Covers: pwd, ls, cd, mkdir, whoami, cat, touch, cp, mv, rm, echo, less, grep,
find, plus File Permissions (chmod, chown) and Process Management (ps, top, kill).

### Recursion chapter

- `recursionintro.rst`: shows recursive *and* iterative factorial/Fibonacci
  side-by-side; both versions validate input with `ValueError` for negative n;
  includes "No Tail-Call Optimisation" and "Security Implications of Unbounded
  Recursion" subsections.
- `recursionexamples.rst`: ends with a "Generators for Sequences with a Ceiling"
  section showing infinite generators + `itertools.takewhile`.

### Case studies chapter (`source/case_studies/`)

Two complete case studies, both using **pandas** and **matplotlib**:

- **Monte Carlo simulation** (`monte_carlo.rst`) — estimates π by throwing random
  darts.  Pipeline: `generate_darts` → `save_darts` → `load_darts` → `estimate_pi`.
  The generate/save/load separation mirrors the Scala workshop design.
  Visualisation in `monte_carlo_plot.py` (scatter plot + convergence grid).
- **Chicago 311 Graffiti** (`graffiti_311.rst`) — full fetch→load→aggregate→filter→
  visualise pipeline against the Chicago Data Portal open dataset.
  The CSV (`311_graffiti.csv`) is gitignored; fetch with:
  `python examples/introcs-python/internet_data/graffiti.py fetch`
  Dataset covers 2011–2018 only (portal stopped updating this view).

### Motivation chapter (`source/context/motivation.rst`)

- Includes "Programming in the Age of Artificial Intelligence" section with
  AGI/human-in-the-loop caveat.
- Includes "Software Engineering, Automation, and Prototyping" section.
- References the Sekharan & Thiruvathukal (2026) op-ed.

---

## Authors

**Lead Editor and Co-Author:** George K. Thiruvathukal (thiruvathukal@gmail.com)

**Faculty Co-Authors:** Konstantin Läufer, Leo Irakliotis

**Contributing Co-Authors (COMP 501 PhD students):** Ihab Al Shaikhli,
Arslan Bisharat, Behnaz Eslami, Matt Hyatt, Jason Luce, Manny Sandoval
Madrigal, Mujtaba Nazari, Erik Pautsch, Michael Saban, Rushikesh Shirsat,
Nicholas Synovic

**Other Contributors:** Thomas W. Christopher (IIT, Emeritus),
Andy Harrington (Loyola, Emeritus)

See `source/appendix/contributors.rst` for the full contributors list.
