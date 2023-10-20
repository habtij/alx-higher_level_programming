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

    @property
    def size(self):
        """returns the size of the square"""
        return (self.__width)

    @size.setter
    def size(self, value):
        """Sets the value of size for the Square"""
        self.integer_validator("width", value)
        self.width = value
        self.integer_validator("height", value)
        self.height = value

    def update(self, *args, **kwargs):
        """Update the value of Square"""
        if len(args) > 0 and args is not None:
            if len(args) >= 4:
                super().__init__(args[0])
                self.integer_validator("width", args[1])
                self.size = args[1]
                self.integer_validator("x", args[2])
                self.x = args[2]
                self.integer_validator("y", args[3])
                self.y = args[3]
            elif len(args) == 3:
                super().__init__(args[0])
                self.integer_validator("width", args[1])
                self.size = args[1]
                self.integer_validator("x", args[2])
                self.x = args[2]
            elif len(args) == 2:
                super().__init__(args[0])
                self.integer_validator("width", args[1])
                self.size = args[1]
            else:
                super().__init__(args[0])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                elif key == "size":
                    self.integer_validator("width", value)
                    self.size = value
                elif key == "x":
                    self.integer_validator(key, value)
                    self.x = value
                elif key == "y":
                    self.integer_validator(key, value)
                    self.y = value
