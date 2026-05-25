.. index:: contributing, contribution guidelines, pull requests, issue tracker

.. _Contributing-Guidelines:

Contributing Guidelines
=======================

Thank you for your interest in contributing to *Introduction to Computer
Science in Python: Principles and Practice*.

This book is primarily a work of faculty from the Loyola University Chicago
Computer Science department, developed to support our program in Computer
Science. Although the material is general in nature, our first priority is to
serve Loyola students and instructors.

What We Are Looking For
-----------------------

Our current effort is best suited to small, focused contributions. The topics
in the book are introductory and are unlikely to be controversial, so our main
interest is in identifying useful topics, subtopics, examples, explanations,
figures, exercises, and corrections that may be missing or unclear.

Good contributions usually do one of the following:

- identify a missing topic or subtopic;
- clarify an explanation for beginning students;
- correct a technical error, typo, broken link, or formatting issue;
- improve an example without adding unnecessary complexity;
- suggest a small exercise, review question, or classroom activity;
- improve accessibility, readability, or consistency.

Please keep proposed changes focused. Large rewrites, broad restructuring, or
major new chapters are harder for us to review and may be deferred even if the
idea is useful.

Start With an Issue
-------------------

For most contributors, we recommend starting with the issue tracker. This is
especially appropriate if your day-to-day workflow does not involve plaintext
writing, reStructuredText, Sphinx, and Git.

When opening an issue, please:

- describe the problem or suggestion clearly;
- point to the relevant chapter or section when possible;
- include proposed wording directly in the issue body if you have it;
- keep the issue focused on one topic;
- avoid attachments such as Word documents, PDFs, slide decks, or screenshots
  unless they are essential.

Plain text is easiest for us to review, quote, edit, and incorporate.

Pull Requests
-------------

Contributors who are comfortable with Git may submit a pull request.

Pull requests should:

- be small and focused;
- use the existing Sphinx/reStructuredText style of the book;
- put longer runnable Python examples in ``examples/introcs-python/<chapter>/``
  and include them with ``literalinclude``;
- keep short teaching fragments inline with ``code-block:: python``;
- preserve the book's introductory level and avoid unnecessary complexity;
- include unit tests for longer code examples when practical, with ``pytest``
  preferred;
- include source or attribution notes when adapting material from elsewhere;
- acknowledge any use of AI systems and briefly describe their role;
- avoid committing generated build output.

We may edit, reorganize, or rewrite accepted contributions so they fit the
book's voice, structure, and curricular goals.

Use of AI Assistance
--------------------

Contributors may use AI systems as part of their writing, editing, coding, or
review workflow, but the use of AI must be acknowledged in the issue or pull
request. The acknowledgment should briefly explain what the AI system helped
with, such as brainstorming, drafting prose, rewriting examples, generating
code, checking grammar, or summarizing source material.

We do not accept AI-only work. Every contribution must have a human contributor
who can explain their own role, the role of any AI system, the origin of the
material, and why the proposed change is appropriate for this book. Contributors
are responsible for checking AI-assisted work for accuracy, originality,
attribution, licensing compatibility, and suitability for beginning students.

Editorial Review and Licensing
------------------------------

All contributions are subject to editorial review by the lead editor, George
K. Thiruvathukal. Submission of an issue, suggestion, or pull request does not
guarantee acceptance.

By contributing, you agree that accepted contributions may be edited,
rewritten, incorporated into the book, and released under the `Creative
Commons Attribution 4.0 International License <https://creativecommons.org/licenses/by/4.0/>`_.
Loyola University Chicago and the Computer Science faculty retain all rights
necessary for continued distribution of the book and may use the materials in
support of the department, including not-for-profit fundraising.

If you are contributing material that was previously published, developed for a
course, or created with collaborators, please make sure you have the right to
submit it and clearly identify any required attribution.

Code of Conduct
---------------

Participation in this project must follow the professional and community
standards reflected in:

- the `Python Software Foundation Code of Conduct <https://policies.python.org/python.org/code-of-conduct/>`_;
- the `ACM Code of Ethics and Professional Conduct <https://www.acm.org/code-of-ethics>`_;
- the `IEEE Code of Conduct <https://events.ieee.org/wp-content/uploads/ieee_code_of_conduct.pdf>`_
  and `IEEE Code of Ethics <https://www.ieee.org/about/corporate/governance/p7-8.html>`_.

We will reject or close issues and pull requests that do not follow these
guidelines. This includes abusive, discriminatory, harassing, hostile, or
unprofessional communication, as well as submissions that fail to give proper
credit for the work of others, including non-human assistance.

Questions
---------

If you are unsure whether a contribution is a good fit, please open an issue
with a short proposal before preparing a pull request.
