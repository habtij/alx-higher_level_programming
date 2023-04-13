#!/usr/bin/python3

""" a module ``0-add_integer`` that contains ``add_integer`` function """


def add_integer(a, b=98):
    """return the sum of a and b"""

    if a is None or (float(a) != a and int(a) != a):
        raise TypeError("a must be an integer")
    elif float(b) != b and int(b) != b:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
