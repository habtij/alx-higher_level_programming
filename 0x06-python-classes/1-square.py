#!/usr/bin/python3
""" Creates a square class with a private attr size"""


class Square:
    """ A square class with private attr size """
    __size
    def __init__(self, new_size):
        """ An initializer method """
        self.__size = new_size
