#!/usr/bin/python3
"""This module ``9-rectangle`` defines a class ``Rectangle`` that
inherits from ``BaseGeometry``
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle and inherits from BaseGeometry"""
    def __init__(self, width, height):
        """
        Initializes a new Rectangle

        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns a string representation of the rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
