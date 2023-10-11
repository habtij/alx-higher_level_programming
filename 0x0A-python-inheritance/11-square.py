#!/usr/bin/python3
"""Defines a class ``Square`` that inherits from Rectangle in
``9-rectangle`` module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square that inherits from Rectangle"""
    def __init__(self, size):
        """Initializes a new square

        Args:
            size (int): The sides of the square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        """returns a string representation of the square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
