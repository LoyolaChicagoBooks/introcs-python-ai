# -*- coding: utf-8 -*-

import sys, os, os.path
from datetime import date

extensions = ['sphinx.ext.todo', 'sphinx.ext.mathjax', 'sphinx.ext.extlinks', 'jupyterlite_sphinx']

extlinks = {
    'repsrc': (
        'https://github.com/LoyolaChicagoBooks/introcs-python-examples/blob/master/%s',
        None,
    )
}

todo_include_todos = True

# jupyterlite-sphinx "Try Examples": selected doctest snippets get a button that
# turns the code into a live, editable JupyterLite cell on the website.  We use
# the directive (`.. try_examples::`) on curated examples rather than enabling it
# globally.  The rendered code shows in every format; only the button is HTML.
try_examples_global_button_text = "Try it live ▶"
try_examples_global_warning_text = (
    "This example runs in your browser via JupyterLite (Pyodide). "
    "It may take a few seconds to start the first time, and your edits "
    "are not saved."
)

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Introduction to Computer Science in Python: Principles and Practice'
author = u'Loyola University Chicago Computer Science Department; Edited by George K. Thiruvathukal'
copyright = u'2026, Loyola University Chicago Computer Science Department'

version = date.today().strftime("%d %b %Y")
release = version

exclude_patterns = ['_build']

pygments_style = 'sphinx'

rst_prolog = """.. highlight:: python
"""

rst_epilog = """
.. |if-else| replace:: ``if``\\ -``else``

.. |if-elif-else| replace:: ``if``\\ -``elif``\\ -``else``

.. |while| replace:: ``while``

"""

html_theme = 'sphinx_book_theme'

html_theme_options = {
    "home_page_in_toc": True,
    "show_toc_level": 2,
    "repository_url": "https://github.com/LoyolaChicagoBooks/introcs-python-ai",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_download_button": False,
}

html_title = f'{project} ({release})'
html_short_title = 'Intro CS in Python'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_logo = '_static/logo.png'
html_last_updated_fmt = '%d-%B-%Y %H:%M:%S'

htmlhelp_basename = 'introcs-python'
highlight_language = 'python'

latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
\setmainfont{FreeSerif.otf}[
  ItalicFont     = FreeSerifItalic.otf,
  BoldFont       = FreeSerifBold.otf,
  BoldItalicFont = FreeSerifBoldItalic.otf
]
\setsansfont{FreeSans.otf}[
  ItalicFont     = FreeSansOblique.otf,
  BoldFont       = FreeSansBold.otf,
  BoldItalicFont = FreeSansBoldOblique.otf
]
\setmonofont{FreeMono.otf}[Scale=0.9,
  ItalicFont     = FreeMonoOblique.otf,
  BoldFont       = FreeMonoBold.otf,
  BoldItalicFont = FreeMonoBoldOblique.otf
]
''',
}

latex_documents = [
    ('index', 'introcs-python.tex',
     u'Introduction to Computer Science in Python:\\\\ Principles and Practice',
     u'Loyola University Chicago Computer Science Department; Edited by George K. Thiruvathukal', 'manual'),
]

epub_basename = 'introcs-python'

# Hide the (non-functional) "Try Examples" run button/iframe in the EPUB.  The
# EPUB builder's format is "html", so the raw-HTML button is not auto-excluded
# the way it is in the LaTeX/PDF build; this stylesheet hides it for EPUB only.
epub_css_files = ['epub-overrides.css']


def _stringify_node_ids(app, doctree):
    """Coerce every node id to ``str``.

    jupyterlite-sphinx's ``.. try_examples::`` directive appends a raw
    ``uuid4()`` *object* (not a string) to a container node's ``ids``.  The HTML
    writer stringifies it, but the EPUB builder's ``fix_ids`` calls
    ``fragment.replace(':', '-')`` on each id and crashes with
    ``'UUID' object has no attribute 'replace'``.  Normalising ids here keeps
    every builder (HTML/EPUB/LaTeX) safe and is idempotent for real string ids.
    """
    from docutils import nodes
    for node in doctree.findall(nodes.Element):
        ids = node.get('ids')
        if ids:
            node['ids'] = [str(i) for i in ids]


def setup(app):
    app.connect('doctree-read', _stringify_node_ids)
