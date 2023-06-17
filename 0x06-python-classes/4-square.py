#!/usr/bin/python3
""" ``4-square``module contains ``Square`` class and ``__size`` attribute """


class Square:
    """
    A class representing a  square.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        __init__(size): Initializes a Square object with a given size.
        area: Returns a square area.
        size(value): Set __size to value
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square with optional 0 value
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        size(size)

    def area(self):
        """ Returns the square of self.__size """
        return (self.__size * self.__size)

    def size(self, value):
        """ Set __size to value """
        self.__size = value
