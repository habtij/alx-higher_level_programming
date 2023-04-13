#!/usr/bin/python3

""" a module ``0-add_integer`` that contains ``add_integer`` function """

def add_integer(a, b=98):
    """return the sum of a and b"""

    if not a or float(a) != a or int(a) != a:
        raise TypeError("a must be an integer")
    elif not b or float(b) != b or int(b) != b:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
