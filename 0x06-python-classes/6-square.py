#!/usr/bin/python3
""" ``5-square``module contains ``Square`` class and ``__size`` attribute """


class Square:
    """
    A class representing a  square.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The tuple of the square (private).

    Methods:
        __init__(size): Initializes a Square object with a given size.
        area(): Returns the area of the square.
        size(value): Set the size of square.
        size(): Retrieve the size of square.
        my_print(): Prints the square with a '#'.
        position(value): Sets the postion of the square.
        position(): Retrieve the value of position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square with optional 0 value
            position (tuple): The position of the square with 
                    optional tuple of (0, 0) values
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) and len(position) != 2 and \
                position[0] < 0 and position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        if self.__position[1] > 0:
            print("")

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                for j in range(self.__size):
                    print("#", end='')
                print()

    @property
    def position(self):
        """ Return the value of position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ set the value of position """
        if not isinstance(value, tuple) and len(value) != 2 \
                and value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
