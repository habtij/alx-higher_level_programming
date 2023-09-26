#!/usr/bin/python3
"""The module creates a square class that contains private size attribute,
area and size getter and setter methods
"""


class Square:
    """A square class that contains a private size attribute, area,
    size getter and setter methods and my_print menthod
    """
    def __init__(self, size=0):
        """Initiliaze the size attribute"""
        self.size = size

    @property
    def size(self):
        """Returns the size of the square"""
        return (self.__size)

    @size.property
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the graphical representation for the square with #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
