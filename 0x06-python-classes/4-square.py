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
        size(size)

    def area(self):
        """ Returns the square of self.__size """
        return (self.__size * self.__size)

    def size(self):
        """ Retrieve the content of ``__size`` """
        return (__self.__size)

    def size(self, value):
        """ Set __size to value """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
