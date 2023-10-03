#!/usr/bin/python3
"""This module define a Node and singlyLinkedList class"""


class Node:
    """A node class that contains private data and next_node attributes,
    data setter and getter methods
    """
    def __init__(self, data, next_node=None):
        """Initialize the data and next_node attributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the value of data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets the value of data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns the value of next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets the value of next_node"""
        if not isinstance(value, Node) or value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list class"""
    def __init__(self):
        self.head = None

    def __str__(self):
        """Prints the entire list"""
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next_node

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list"""
        if self.head is None and value is not None:
            self.head = Node(value)
        else:
            temp = self.head
            while temp is not None:
                if value < temp.data:
                    self.head.data = value
