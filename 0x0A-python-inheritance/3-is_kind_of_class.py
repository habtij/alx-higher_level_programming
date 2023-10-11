#!/usr/bin/python3
"""This module ``3-is_kind_of_class`` defines a function 
``is_kind_of_class`` that returns a boolean
"""


def is_kind_of_class(obj, a_class):
    """Returns a boolean if an object is an instance of a class that
    inherits from, the specified class
    """
    return (isinstance(obj, a_class)
