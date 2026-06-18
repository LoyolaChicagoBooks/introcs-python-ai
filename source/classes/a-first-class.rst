.. index:: class; Contact, OOP; __init__, self, instance variable
   ACM-IEEE CS2013; PL1 Object-Oriented Programming
   ACM-IEEE CS2023; PL1 Object-Oriented Programming

.. _First-Class:

A First Example of Class Instances
====================================

We have used many built-in types and library classes.  Now we define our
own.  As a first example, a *contact* has a name, phone number, and email
address — three pieces of data that belong together as one entity.

Defining the Class
------------------

.. index:: class; keyword, __init__, self

.. code-block:: python

   class Contact:
       def __init__(self, name: str, phone: str, email: str):
           self.name = name
           self.phone = phone
           self.email = email

- ``class Contact:`` declares a new type named ``Contact``.
- ``__init__`` is the *initialiser* — Python calls it automatically when a
  new object is created.
- ``self`` is the first parameter of every instance method.  It refers to
  the specific object being created or operated on.  You never pass it
  explicitly; Python fills it in.
- ``self.name = name`` stores the argument in an *instance variable* —
  data that lives as long as the object exists.

Creating Instances
------------------

.. index:: class; instantiation

.. code-block:: python

   c = Contact("Marie Ortiz", "773-508-7890", "mortiz2@luc.edu")

This creates a new ``Contact`` object and binds it to ``c``.  Each object
has its own copy of the instance variables.

Accessing Instance Variables
-----------------------------

.. index:: instance variable; access

Run this to create a ``Contact`` and read back each of its instance
variables — try changing the values:

.. try_examples::
   :height: 280px

   >>> class Contact:
   ...     def __init__(self, name: str, phone: str, email: str):
   ...         self.name = name
   ...         self.phone = phone
   ...         self.email = email
   ...
   >>> c = Contact("Marie Ortiz", "773-508-7890", "mortiz2@luc.edu")
   >>> print(c.name)
   Marie Ortiz
   >>> print(c.phone)
   773-508-7890
   >>> print(c.email)
   mortiz2@luc.edu

Adding a ``__str__`` Method
-----------------------------

.. index:: __str__, string representation

``__str__`` is called automatically whenever Python needs a string
representation of the object (e.g., inside ``print()``):

.. literalinclude:: ../../examples/introcs-python/classes/contact.py
   :language: python
   :start-after: # start: Contact
   :end-before: # end: Contact

Run this version, which defines the class with ``__str__`` and then prints
an instance:

.. try_examples::
   :height: 320px

   >>> class Contact:
   ...     def __init__(self, name: str, phone: str, email: str):
   ...         self.name = name
   ...         self.phone = phone
   ...         self.email = email
   ...     def __str__(self) -> str:
   ...         return (f"Name:  {self.name}\n"
   ...                 f"Phone: {self.phone}\n"
   ...                 f"Email: {self.email}")
   ...
   >>> c = Contact("Marie Ortiz", "773-508-7890", "mortiz2@luc.edu")
   >>> print(c)
   Name:  Marie Ortiz
   Phone: 773-508-7890
   Email: mortiz2@luc.edu

Adding Methods
--------------

.. index:: instance method

Instance methods work exactly like functions, but receive ``self`` as
their first argument.  We can add a method to update the email address:

.. code-block:: python

       def set_email(self, new_email: str) -> None:
           self.email = new_email

Run this to call the method and confirm the email address changed:

.. try_examples::
   :height: 300px

   >>> class Contact:
   ...     def __init__(self, name: str, phone: str, email: str):
   ...         self.name = name
   ...         self.phone = phone
   ...         self.email = email
   ...     def set_email(self, new_email: str) -> None:
   ...         self.email = new_email
   ...
   >>> c = Contact("Marie Ortiz", "773-508-7890", "mortiz2@luc.edu")
   >>> c.set_email("maria.ortiz@gmail.com")
   >>> print(c.email)
   maria.ortiz@gmail.com

.. index:: name mangling, single underscore convention

Privacy by Convention
---------------------

.. index:: _name convention, OOP; private

Python has no ``private`` keyword.  The convention is to prefix an
attribute with a single underscore (``_name``) to signal that it is
intended for internal use and should not be accessed directly from
outside the class.  Double underscore (``__name``) invokes *name
mangling*, which makes accidental access harder.

For the Contact class this is a matter of taste; we leave the attributes
public since this is a simple data container.

Using a List of Contacts
-------------------------

.. index:: list; of class instances

.. code-block:: python

   contacts = [
       Contact("Marie Ortiz", "773-508-7890", "mortiz2@luc.edu"),
       Contact("Otto Heinz",  "773-508-9999", "oheinz@luc.edu"),
   ]

   for contact in contacts:
       print(contact)
       print()
