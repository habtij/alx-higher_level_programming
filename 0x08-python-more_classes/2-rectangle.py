#!/usr/bin/python3
"""This module creates a rectangle class with private attr width"""


class Rectangle:
    """
    A class representing a Rectangle.

    Attribute:
    __width (int): The width of the rectangle (private).
    __height (int): The height of the rectangle (private).

    Method:
    __init__ (width, height): Initializes a Rectangle object with specified
        width and height
    width(): Retrieves the width of the rectangle.
    width(value): Set the width of the rectangle to value.
    height(): Retrieves the height of the rectangle.
    height(value): Set the height of the rectangle to value.
    area(): Retrieves the area of rectangle.
    perimeter(): Retrieves the perimeter of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle object with the width and height

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return (self.__width + self.__height)
