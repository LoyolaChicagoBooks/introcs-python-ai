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
