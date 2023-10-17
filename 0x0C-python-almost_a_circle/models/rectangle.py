#!/usr/bin/python3
"""Defines a ``Rectangle`` class and inherit from ``Base`` class"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the instance

        Args:
            __width (int): The width of the rectangle (private)
            __height (int): The height of the rectangle (private)
            __x (int): x coordinate of the rectangle (private)
            __y (int): y coordinate of the rectangle (private)

        Methods:
            width(): retrieves the value of width.
            width(value): sets the value of width.
            height(): retrieves the value of height.
            height(value): sets the value of height.
            x(): retrieves the value of x coordinate.
            x(value): sets the value of x coordinate.
            y(): retrieves the value of y coordinate.
            y(value): sets the value of y coordinate.
            __init__(width, height, x=0, y=0, id=None): Initializes the
                Rectangle.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the value of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        self.__height = value

    @property
    def x(self):
        """Retrieves the value x coordinate"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Sets the value of x coordinate"""
        self.__x = value

    @property
    def y(self):
        """Retrieves the value of y coordinate"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Sets the value of y coordinate"""
        self.__y = value