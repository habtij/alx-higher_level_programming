#!/usr/bin/python3
"""This module creates a rectangle class with private attribute
width and height"""


class Rectangle:
    """Define a rectangle class with private attribute width & height"""
    def __init__(self, width=0, height=0):
        """Initialize the private attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the value of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
