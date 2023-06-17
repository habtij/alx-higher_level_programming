#!/usr/bin/python3
""" ``2-square`` contains ``Square`` class and ``__size`` attribute """


class Square:
    """ A ``Square`` class with private attribute ``__size`` """
    __size

    def __init__(self, size=0):
        """ An initializer with ``__size`` attribute """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__self = size
