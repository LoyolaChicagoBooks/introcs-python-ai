.. index:: linked list, Node class, singly linked list

.. _Linked-Lists:

Linked Lists
============

A *linked list* stores elements in nodes, where each node holds a value
and a reference to the next node.  Unlike Python's built-in list, a
linked list does not require a contiguous block of memory.

The Node Class
--------------

.. index:: Node class

.. code-block:: python

   class Node:
       def __init__(self, data, next_node: "Node | None" = None):
           self.data = data
           self.next = next_node

Each node points to the next node in the chain.  The last node's
``next`` is ``None`` — the Python equivalent of a null pointer.

Building a Linked List by Hand
--------------------------------

.. index:: linked list; construction

.. code-block:: python

   # Build the list  1 -> 2 -> 3 -> None
   head = Node(1, Node(2, Node(3)))

Traversal
---------

.. index:: linked list; traversal

Walk the list by following ``next`` until ``None``:

.. literalinclude:: ../../examples/introcs-python/datastructures/linked_list.py
   :language: python
   :start-after: # start: print_list
   :end-before: # end: print_list

Run the whole thing — node class, traversal, and a hand-built list together:

.. try_examples::
   :height: 340px

   >>> class Node:
   ...     def __init__(self, data, next_node: "Node | None" = None):
   ...         self.data = data
   ...         self.next = next_node
   ...
   >>> def print_list(head: "Node | None") -> None:
   ...     current = head
   ...     while current is not None:
   ...         print(current.data, end=" -> ")
   ...         current = current.next
   ...     print("None")
   ...
   >>> head = Node(1, Node(2, Node(3)))
   >>> print_list(head)
   1 -> 2 -> 3 -> None

The SinglyLinkedList Class
--------------------------

.. index:: SinglyLinkedList

A wrapper class manages the ``head`` pointer and provides clean methods:

.. literalinclude:: ../../examples/introcs-python/datastructures/linked_list.py
   :language: python
   :start-after: # start: SinglyLinkedList
   :end-before: # end: SinglyLinkedList

.. code-block:: python

   lst = SinglyLinkedList()
   lst.append(10)
   lst.append(20)
   lst.append(30)
   lst.prepend(5)
   print(lst)

   lst.remove(20)
   print(lst)

Output:

.. code-block:: none

   5 -> 10 -> 20 -> 30 -> None
   5 -> 10 -> 30 -> None

.. index:: dynamic array; vs linked list, Big-O notation; data structures

Performance Comparison
-----------------------

.. index:: linked list; performance

+-------------------+------------+------------+
| Operation         | List       | LinkedList |
+===================+============+============+
| Index access      | O(1)       | O(N)       |
+-------------------+------------+------------+
| Prepend           | O(N)       | O(1)       |
+-------------------+------------+------------+
| Append            | O(1) amort | O(N)       |
+-------------------+------------+------------+
| Insert in middle  | O(N)       | O(N)       |
+-------------------+------------+------------+
| Remove from front | O(N)       | O(1)       |
+-------------------+------------+------------+

Python's built-in list is a dynamic array and is faster for most uses.
Linked lists shine when you need O(1) prepend or frequent insertions at
a known position.
