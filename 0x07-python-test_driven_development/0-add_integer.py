#!/usr/bin/python3

def add_integer(a, b=98):
    """return the sum of a and b"""

    if not a or int(a) != a or float(a) != a:
        raise TypeError("a must be an integer")
    elif not b int(b) != b or float(b) != b:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
