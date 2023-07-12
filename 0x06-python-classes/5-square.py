#!/usr/bin/python3
""" ``5-square``module contains ``Square`` class and ``__size`` attribute """


class Square:
    """
    A class representing a  square.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        __init__(size): Initializes a Square object with a given size.
        area(): Returns the area of the square.
        size(value): Set the size of square.
        size(): Retrieve the size of square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square with optional 0 value
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Returns the area of the square """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ Return the value of size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Set size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Prints a square with # symbol """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
