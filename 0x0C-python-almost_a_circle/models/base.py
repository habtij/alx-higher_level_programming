#!/usr/bin/python3
"""Defines a ``Base`` class"""


class Base:
    """
    A class representing the base

    Attribute:
        __nb_objects (int): Number of objects created (private class attr)
        id (int): Public instance attribute
    Method:
        __init__(id): Initializes a object with given id or None
        integer_validator(name, value): validates the value
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base object with the given id

        Args:
            id (int): The id of the object
        """
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects

    def integer_validator(self, name, value):
        """Validates the value, and raise an exception if there is error"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be > 0".format(name))
