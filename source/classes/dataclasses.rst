.. index:: dataclass, @dataclass, namedtuple

.. _Dataclasses:

Python Dataclasses and Named Tuples
====================================


Writing a data-holding class by hand requires repeating each field name
three or four times — in ``__init__`` parameters, in ``self.x = x``
assignments, and in ``__repr__``.  The ``@dataclass`` decorator generates
all of this automatically from a simple field declaration.

Basic Dataclass
---------------

.. index:: @dataclass; basic

.. code-block:: python

   from dataclasses import dataclass

   @dataclass
   class Contact:
       name: str
       phone: str
       email: str

.. index:: @dataclass; generated methods, boilerplate elimination

This single declaration is equivalent to:

.. code-block:: python

   class Contact:
       def __init__(self, name: str, phone: str, email: str):
           self.name = name
           self.phone = phone
           self.email = email

       def __repr__(self):
           return f"Contact(name={self.name!r}, phone={self.phone!r}, email={self.email!r})"

       def __eq__(self, other):
           return (self.name, self.phone, self.email) == (other.name, other.phone, other.email)

Here we create a ``Contact`` instance and verify that display and equality
work without any extra code — run it to see the generated ``__repr__`` and
``__eq__`` in action:

.. try_examples::
   :height: 280px

   >>> from dataclasses import dataclass
   >>> @dataclass
   ... class Contact:
   ...     name: str
   ...     phone: str
   ...     email: str
   ...
   >>> c = Contact("Marie Ortiz", "773-508-7890", "mortiz2@luc.edu")
   >>> print(c)
   Contact(name='Marie Ortiz', phone='773-508-7890', email='mortiz2@luc.edu')
   >>> print(c == Contact("Marie Ortiz", "773-508-7890", "mortiz2@luc.edu"))
   True

Default Values
--------------

.. index:: @dataclass; defaults

Fields can have default values, just like function parameters.  Run this and
try omitting or supplying the coordinates:

.. try_examples::
   :height: 260px

   >>> from dataclasses import dataclass
   >>> @dataclass
   ... class Point:
   ...     x: float = 0.0
   ...     y: float = 0.0
   ...
   >>> origin = Point()
   >>> p = Point(3.0, 4.0)
   >>> print(origin, p)
   Point(x=0.0, y=0.0) Point(x=3.0, y=4.0)

Adding Methods
--------------

.. index:: @dataclass; methods

You can still add your own methods — ``@dataclass`` only generates the
boilerplate:

.. code-block:: python

   import math

   @dataclass
   class Point:
       x: float
       y: float

       def distance_to(self, other):
           return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

       def __str__(self):
           return f"({self.x}, {self.y})"

Immutable Dataclasses
----------------------

.. index:: @dataclass; frozen

Pass ``frozen=True`` to make instances immutable (and hashable, so they
can be used as dictionary keys):

.. code-block:: python

   @dataclass(frozen=True)
   class Point:
       x: float
       y: float

   p = Point(1.0, 2.0)
   # p.x = 5.0   # raises FrozenInstanceError

Named Tuples
------------

.. index:: namedtuple, collections; namedtuple

A *named tuple* is a tuple subclass whose fields have names as well as
positions.  It comes from the ``collections`` module and requires no
class body at all — you describe the fields in a single line:

.. code-block:: python

   from collections import namedtuple

   Point = namedtuple('Point', ['x', 'y'])

``Point`` is now a full type.  You create instances the same way you
would call a constructor.  Run this to see named-field and positional access
side by side:

.. try_examples::
   :height: 280px

   >>> from collections import namedtuple
   >>> Point = namedtuple('Point', ['x', 'y'])
   >>> p = Point(3.0, 4.0)
   >>> print(p)
   Point(x=3.0, y=4.0)
   >>> print(p.x, p.y)
   3.0 4.0
   >>> print(p[0], p[1])   # positional access still works
   3.0 4.0

Because a named tuple *is* a tuple, unpacking, indexing, and iteration
all work exactly as with a plain tuple.

Immutability and Hashing
^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: namedtuple; immutable, namedtuple; hashable

Named tuples are immutable — you cannot reassign a field after
creation:

.. code-block:: python

   p = Point(1.0, 2.0)
   # p.x = 5.0   # raises AttributeError

Because they are immutable they are also *hashable*, so they can be
used as dictionary keys, just like plain tuples.  Run this to look one up:

.. try_examples::
   :height: 240px

   >>> from collections import namedtuple
   >>> Point = namedtuple('Point', ['x', 'y'])
   >>> labels = {Point(0, 0): "origin", Point(1, 0): "east"}
   >>> print(labels[Point(0, 0)])
   origin

Creating Modified Copies with ``_replace``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: namedtuple; _replace

Since you cannot mutate a named tuple in place, the ``_replace`` method
returns a *new* instance with chosen fields changed.  Run this and note that
``p`` is unchanged:

.. try_examples::
   :height: 240px

   >>> from collections import namedtuple
   >>> Point = namedtuple('Point', ['x', 'y'])
   >>> p = Point(3.0, 4.0)
   >>> q = p._replace(y=0.0)
   >>> print(p, q)
   Point(x=3.0, y=4.0) Point(x=3.0, y=0.0)

Reworking the Contact Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: namedtuple; Contact example

The ``Contact`` class from the previous section becomes a one-liner.  Run it:

.. try_examples::
   :height: 260px

   >>> from collections import namedtuple
   >>> Contact = namedtuple('Contact', ['name', 'phone', 'email'])
   >>> c = Contact("Marie Ortiz", "773-508-7890", "mortiz2@luc.edu")
   >>> print(c)
   Contact(name='Marie Ortiz', phone='773-508-7890', email='mortiz2@luc.edu')
   >>> print(c.name)
   Marie Ortiz

This is ideal when a contact record is read-only data being passed
around the program.  If you need to update a contact's email, use
``_replace``; if you need validation logic in ``__init__``, use a full
class or ``@dataclass``.

Reworking the Point Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: namedtuple; Point example

``Point`` as a named tuple gives you named-field access, a readable
``repr``, equality comparison, and hashability — all for free.  Run it:

.. try_examples::
   :height: 320px

   >>> import math
   >>> from collections import namedtuple
   >>> Point = namedtuple('Point', ['x', 'y'])
   >>> def distance(p1: Point, p2: Point) -> float:
   ...     return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
   ...
   >>> origin = Point(0, 0)
   >>> p = Point(3, 4)
   >>> print(distance(origin, p))
   5.0
   >>> print(origin == Point(0, 0))   # value equality, like tuples
   True

The trade-off: because ``namedtuple`` produces a true tuple subclass,
you cannot attach methods directly to it the way you can with a class.
The ``distance`` function above is a standalone function rather than a
method — a reasonable choice for simple geometric helpers, but
awkward for richer objects.

Choosing the Right Tool
-----------------------

.. index:: namedtuple; vs dataclass, @dataclass; when to use

Python offers several ways to bundle related data, each with a
different trade-off between simplicity, mutability, and power:

**Plain tuple** — use when the structure is anonymous and throwaway,
or when the positional meaning is universally obvious (e.g., ``(x, y)``
in a tiny helper).  No named access, no repr, no type hint.

**Named tuple** — use for lightweight, *immutable* records where named
field access matters and no behaviour is needed.  Zero boilerplate, a
clean repr, hashable by default.  Good for coordinates, colours, simple
value objects.

.. code-block:: python

   Color = namedtuple('Color', ['r', 'g', 'b'])
   red = Color(255, 0, 0)

**Dataclass** — use when fields need defaults, mutability, or a small
amount of domain logic (methods).  ``frozen=True`` gives you the same
immutability and hashability as a named tuple but with richer
annotation support.

.. code-block:: python

   @dataclass
   class Point:
       x: float
       y: float

       def distance_to(self, other):
           return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

**Full class** — use when initialisation requires validation, when
attributes must be kept private, when inheritance is involved, or when
the object has complex mutable state that changes over its lifetime.

.. list-table:: Data container options at a glance
   :header-rows: 1
   :widths: 20 16 16 16 16 16

   * - Feature
     - tuple
     - namedtuple
     - @dataclass
     - @dataclass(frozen)
     - class
   * - Named fields
     - No
     - Yes
     - Yes
     - Yes
     - Yes
   * - Mutable
     - No
     - No
     - Yes
     - No
     - Yes
   * - Hashable
     - Yes
     - Yes
     - No
     - Yes
     - No *
   * - Methods
     - No
     - Limited **
     - Yes
     - Yes
     - Yes
   * - Boilerplate
     - None
     - One line
     - Decorator
     - Decorator
     - Full body

\* Unless ``__hash__`` is defined manually.

\*\* Methods can be added via subclassing, but it is uncommon.

When in doubt: start with a named tuple.  If you find yourself
wanting defaults, mutation, or methods, switch to ``@dataclass``.  If
you need private state or validation logic, write a full class.
