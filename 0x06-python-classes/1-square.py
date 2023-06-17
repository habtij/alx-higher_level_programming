#!/usr/bin/python3
""" Creates a square class with a private attr size"""


class Square:
    """
    A class representing a square.

    Attribute:
        __size (int): The size of the square (private).

    Methods:
        __init__(new_size): Initializes a Square object with a given size.
    """

    def __init__(self, new_size):
        """
        Initializes a Square object with a given size.

        Args:
            new_size (int): The size of the square.
        """
        self.__size = new_size
