#!/usr/bin/python3
"""The module creates a square class with size attribute, area,
size getter & setter, my_print and position getter and setter method
"""


class Square:
    """A square class that contains private size and position attribute,
    size and position getter and setter, my_print and area method
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initiliaze size and position attribute for square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of size for square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the value of the position for square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the value of the position for square"""
        if not isinstance(value, tuple) and (value[0] < 0 and value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Return the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
