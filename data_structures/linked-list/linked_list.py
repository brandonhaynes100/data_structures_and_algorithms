from node import Node
from typing import Any, Iterable


class LinkedList(object):

    def __init__(self, input_iterable=None) -> Node:
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

    # def __next__(self):
    #     pass

    # Type annotations (python3.6+)
    # expected return value -> Any
    # defines output for intellisense
    def insert(self, val: Any) -> Any:
        new_node = Node(val, self.head)
        self.head = new_node
        self._len += 1

    # expected return value -> bool
    def includes(self, val: Any) -> bool:
        iter_node = self.__iter__()
        if iter_node.val == val:
            return True
        while iter_node.val:
            if iter_node.val == val:
                return True
            iter_node = iter_node._next
        else:
            return False
