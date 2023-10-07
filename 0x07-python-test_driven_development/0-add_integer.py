#!/usr/bin/python3
"""This module contain an addition function"""


def add_integer(a, b=98):
    """Return the summation of the first and second argument"""
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(a, int) or not isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a + b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
