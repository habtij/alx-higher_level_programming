#!/usr/bin/python3
"""This module ``4-inherits_from`` defines a function ``inherits_from``
that returns a boolean
"""


def inherits_from(obj, a_class):
    """Returns a boolean if the object is an instance of a class that
    inherited(directly or indirectly from the specified class
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
