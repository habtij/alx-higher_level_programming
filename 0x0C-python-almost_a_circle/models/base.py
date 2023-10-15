#!/usr/bin/python3
"""Defines a ``Base`` class"""


class Base:
    """
    A class representing the base

    Attribute:
        __nb_objects (int): Number of objects created (private class attr)
        id (int): Public instance attribute
    Method:
        __init__ (id): Initializes a object with given id or None
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
