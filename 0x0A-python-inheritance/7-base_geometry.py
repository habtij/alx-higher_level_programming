#!/usr/bin/python3
"""This module ``5-base_geometry`` defines a class ``BaseGeometry"""


class BaseGeometry:
    """Represents a Base Geometry that contains public instance
    method area

    Methods:
        area(): raises an exception
        integer_validator(name, value): validates the value
    """
    def area(self):
        """Function raises an exception only"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
