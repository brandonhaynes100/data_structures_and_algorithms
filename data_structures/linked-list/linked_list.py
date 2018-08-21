from node import Node
from typing import Any, Iterable


class LinkedList(object):

    def __init__(self, input_iterable=None) -> Node:
        """
        """
        self.head = None
        self._len = 0
        if input_iterable is Iterable:
            for val in input_iterable:
                pass

    def __len__(self):
        return self._len

    def __str__(self):
        return 'Head: {head} | Length: {length}'.format(head=self.head, length=self._len)

    def __repr__(self):
        return '<Linked List | Head: {head} | Length: {length}'.format(head=self.head, length=self._len)

    def __iter__(self):
        return Node(self.head.val, self.head._next)

    # Type annotations (python3.6+)
    # expected return value -> Any
    # defines output for intellisense
    def insert(self, val: Any) -> Any:
        """
        Takes any value as an argument and adds that value 
        to the head of the list with an O(1) Time performance.
        """
        self.head = Node(val, self.head)
        self._len += 1

        return self.head.val

    # expected return value -> bool
    def includes(self, val: Any) -> bool:
        """
        """
        current = self.head

        while current is not None:
            if current.val == val:
                return True
            current = current._next

        return False

    # Code Challenge 06
    def append(self, val):
        """Adds a new node with the given value to the end of the list
        """
        current = self.head
        if not current:
            self.head = Node(val)
            return self

        while current._next is not None:
            current = current._next
        current._next = Node(val)

    def insert_before(self, val, new_val):
        """Adds a new node with the given new_val immediately
        before the first val node
        """
        current = self.head
        if not current:
            self.head = Node(val)
            return self

        while current._next is not None:
            if current._next.val == val:
                new_node = Node(new_val, current._next)
                current._next = new_node
                return self
        # reaching here means the value was not in the linked list
        return self

    def insert_after(self, val, new_val):
        """Adds a new node with the given new_val immediately
        after the first val node
        """
        current = self.head
        if not current:
            self.head = Node(val)
            return self

        while current is not None:
            if current.val == val:
                new_node = Node(new_val, current._next)
                current._next = new_node
                return self
        # reaching here means the value was not in the linked list
        return self
