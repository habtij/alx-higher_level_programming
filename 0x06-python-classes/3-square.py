#!/usr/bin/python3
"""The module creates a square class with size attribute and area method"""


class Square:
    """A square class with private attribute size and method area"""
    def __init__(self, size):
        """Initialize square attribute size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the area of square"""
        return (self.__size ** 2)
