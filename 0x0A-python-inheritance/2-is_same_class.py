#!/usr/bin/python3
"""The module ``2-is_same_class`` defines function ``is_same_class`` that
returns boolean
"""


def is_same_class(obj, a_class):
    """Returns boolean when an object is exactly an instance a specified
    class
    """
    if type(obj) == a_class:
        return True
    return False
