#!/usr/bin/python3
"""The module creates a square class with size attribute"""


class Square:
    """A square class with size attribute"""
    def __init__(self, size=0):
        """Initialize the private size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
