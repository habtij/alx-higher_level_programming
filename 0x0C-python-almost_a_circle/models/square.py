#!/usr/bin/python3
"""This module defines a ``Square`` and inherits from ``Rectangle``"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square and inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the Square

        Args:
            size (int): represents the size of the Square
            x (int): represents the x coordinate
            y (int): represents the y coordinate
            id (int): represents the number of instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a custom print statement"""
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))
