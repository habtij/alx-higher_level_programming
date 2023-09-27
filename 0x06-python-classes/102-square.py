#!/usr/bin/python3
"""The module creates a square class with size attribute, area
and size getter and setter methods
"""


class Square:
    """A square class with size private attribute, area and size
    getter and setter methods
    """
    def __init__(self, size=0):
        """it initiliaze size attribute"""
        self.size = size

    @property
    def size(self):
        """returns the size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of square"""
        return (self.__size ** 2)

    def __lt__(self, other):
        """Checks if the area of current square is less than the other"""
        if self.area() < other.area():
            return True
        else:
            return False

    def __eq__(self, other):
        """Checks if the area of the squares is equal"""
        if self.area() == other.area():
            return True
        else:
            return False

    def __ne__(self, other):
        """Checks if the area are not equal"""
        if self.area() != other.area():
            return True
        else:
            return False

    def __le__(self, other):
        """Checks if current area < other area"""
        if self.area() <= other.area():
            return True
        else:
            return False

    def __gt__(self, other):
        """Checks if the current area > other area"""
        if self.area() > other.area():
            return True
        else:
            return False

    def __ge__(self, other):
        """Checks if the current area >= other area"""
        if self.area() >= other.area():
            return True
        else:
            return False
