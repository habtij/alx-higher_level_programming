#!/usr/bin/python3
"""The module creates a square class with size attribute, area
and size getter and setter methods
"""


class Square:
    """A square class with size private attribute, area and size
    getter and setter methods
    """
    def __init__(self, size=0):
        """it initiliaze size attribute"""
        self.size = size

    @property
    def size(self):
        """returns the size of square"""
        return (self.__size)
    @size.setter
    def size(self, value):
        """Sets the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """returns the area of square"""
        return (self.__size ** 2)
