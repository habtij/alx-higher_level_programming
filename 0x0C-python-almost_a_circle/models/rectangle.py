#!/usr/bin/python3
"""Defines a ``Rectangle`` class and inherit from ``Base`` class"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the instance

        Args:
            __width (int): The width of the rectangle (private)
            __height (int): The height of the rectangle (private)
            __x (int): x coordinate of the rectangle (private)
            __y (int): y coordinate of the rectangle (private)

        Methods:
            width(): retrieves the value of width.
            width(value): sets the value of width.
            height(): retrieves the value of height.
            height(value): sets the value of height.
            x(): retrieves the value of x coordinate.
            x(value): sets the value of x coordinate.
            y(): retrieves the value of y coordinate.
            y(value): sets the value of y coordinate.
            __init__(width, height, x=0, y=0, id=None): Initializes the
                Rectangle.
            area(): return the area of the Rectangle.
            display(): prints in stdout the Rectangle instance with #
            __str__(): returns a custom print
            update(*args, **kwargs): Updates the given values of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the value of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        self.integer_validator("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        self.integer_validator("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the value x coordinate"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Sets the value of x coordinate"""
        self.integer_validator("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the value of y coordinate"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Sets the value of y coordinate"""
        self.integer_validator("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.x, end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Return a custom print"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Update the Rectangle class"""
        if len(args) > 0 and args is not None:
            if len(args) >= 5:
                super().__init__(args[0])
                self.integer_validator("width", args[1])
                self.width = args[1]
                self.integer_validator("height", args[2])
                self.height = args[2]
                self.integer_validator("x", args[3])
                self.x = args[3]
                self.integer_validator("y", args[4])
                self.y = args[4]
            elif len(args) == 4:
                super().__init__(args[0])
                self.integer_validator("width", args[1])
                self.width = args[1]
                self.integer_validator("height", args[2])
                self.height = args[2]
                self.integer_validator("x", args[3])
                self.x = args[3]
            elif len(args) == 3:
                super().__init__(args[0])
                self.integer_validator("width", args[1])
                self.width = args[1]
                self.integer_validator("height", args[2])
                self.height = args[2]
            elif len(args) == 2:
                super().__init__(args[0])
                self.integer_validator("width", args[1])
                self.width = args[1]
            else:
                super().__init__(args[0])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                elif key == "width":
                    self.integer_validator(key, value)
                    self.width = value
                elif key == "height":
                    self.integer_validator(key, value)
                    self.height = value
                elif key == "x":
                    self.integer_validator(key, value)
                    self.x = value
                elif key == "y":
                    self.integer_validator(key, value)
                    self.y = value
