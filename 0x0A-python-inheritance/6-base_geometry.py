#!/usr/bin/python3
"""This module ``5-base_geometry`` defines a class ``BaseGeometry"""


class BaseGeometry:
    """Represents a Base Geometry that contains public instance
    method area

    Methods:
        area(): raises an exception the a message
    """
    def area(self):
        """Function raises an exception only"""
        raise Exception("area() is not implemented")
