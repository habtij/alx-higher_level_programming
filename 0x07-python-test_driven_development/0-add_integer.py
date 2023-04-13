#!/usr/bin/python3

""" a module ``0-add_integer`` that contains ``add_integer`` function """


def add_integer(a, b=98):
    """return the sum of a and b"""

    if a is None or (type(a) is not float or type(a) is not int):
        raise TypeError("a must be an integer")
    elif float(b) != b or int(b) != b:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
