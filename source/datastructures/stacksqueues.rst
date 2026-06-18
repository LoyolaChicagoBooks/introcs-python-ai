.. index:: stack, queue, collections.deque
   ACM-IEEE CS2013; SDF3 Fundamental Data Structures
   ACM-IEEE CS2023; SDF3 Fundamental Data Structures
   ACM-IEEE CS2013; AL3 Fundamental Data Structures and Algorithms
   ACM-IEEE CS2023; AL3 Fundamental Data Structures and Algorithms

.. _Stacks-Queues:

Stacks and Queues
=================

.. index:: abstract data type, ADT

Stacks and queues are *abstract data types* — they define what operations
are available, not how they are implemented.

Stacks (LIFO)
-------------

.. index:: stack; LIFO, push, pop

A *stack* follows **Last-In, First-Out** order: the most recently added
item is the first to be removed, like a stack of plates.

Operations:

- **push**: add an item to the top
- **pop**: remove and return the top item
- **peek**: inspect the top item without removing it
- **is_empty**: check whether the stack is empty

.. index:: list; as stack, O(1); list.append and pop

**Using a Python list as a stack:**

Run this to watch the stack grow and shrink — edit the pushes and re-run:

.. try_examples::
   :height: 280px

   >>> stack = []
   >>> stack.append(1)    # push
   >>> stack.append(2)
   >>> stack.append(3)
   >>> print(stack[-1])   # peek: 3
   3
   >>> print(stack.pop()) # pop: 3
   3
   >>> print(stack.pop()) # pop: 2
   2
   >>> print(stack)       # [1]
   [1]

``list.append()`` adds to the end (top); ``list.pop()`` removes from the
end — both O(1).

A Stack Class
^^^^^^^^^^^^^

.. index:: Stack class

Wrapping the list in a class gives a cleaner interface:

.. literalinclude:: ../../examples/introcs-python/datastructures/stack.py
   :language: python
   :start-after: # start: Stack
   :end-before: # end: Stack

Application: Checking Balanced Brackets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: balanced brackets; stack

A classic stack use-case: verify that brackets are correctly matched:

.. literalinclude:: ../../examples/introcs-python/datastructures/stack.py
   :language: python
   :start-after: # start: is_balanced
   :end-before: # end: is_balanced

Run it on a few strings — try one with mismatched brackets of your own:

.. try_examples::
   :height: 360px

   >>> class Stack:
   ...     def __init__(self):
   ...         self._items = []
   ...     def push(self, item):
   ...         self._items.append(item)
   ...     def pop(self):
   ...         return self._items.pop()
   ...     def is_empty(self):
   ...         return len(self._items) == 0
   ...
   >>> def is_balanced(s: str) -> bool:
   ...     stack = Stack()
   ...     pairs = {")": "(", "]": "[", "}": "{"}
   ...     for ch in s:
   ...         if ch in "([{":
   ...             stack.push(ch)
   ...         elif ch in ")]}":
   ...             if stack.is_empty() or stack.pop() != pairs[ch]:
   ...                 return False
   ...     return stack.is_empty()
   ...
   >>> print(is_balanced("({[]})"))
   True
   >>> print(is_balanced("({[})"))
   False

Queues (FIFO)
-------------

.. index:: queue; FIFO, enqueue, dequeue, collections.deque

A *queue* follows **First-In, First-Out** order: like a line of people
waiting, the first to join is the first to leave.

Operations:

- **enqueue**: add an item to the back
- **dequeue**: remove and return the front item
- **is_empty**: check whether the queue is empty

**Using ``collections.deque``:**

.. index:: deque; O(1) both ends, collections.deque; efficiency

A Python list is slow for dequeue (removing from the front is O(N)).
``collections.deque`` supports O(1) operations at both ends:

Run this to see the queue serve people in arrival order:

.. try_examples::
   :height: 300px

   >>> from collections import deque
   >>> queue = deque()
   >>> queue.append("Alice")    # enqueue
   >>> queue.append("Bob")
   >>> queue.append("Carol")
   >>> print(queue.popleft())   # dequeue: Alice
   Alice
   >>> print(queue.popleft())   # dequeue: Bob
   Bob
   >>> print(queue)             # deque(['Carol'])
   deque(['Carol'])

A Queue Class
^^^^^^^^^^^^^

.. index:: Queue class

.. literalinclude:: ../../examples/introcs-python/datastructures/queue.py
   :language: python
   :start-after: # start: Queue
   :end-before: # end: Queue
