#!/usr/bin/python3
"""This module ``1-my_list`` define a ``MyList`` class that inherits from
``list``
"""


class MyList(list):
    """The class ``MyList`` inherits from ``list`` and also created a
    public method ``print_sorted``
    """
    def print_sorted(self):
        """prints iterables in sorted ascending order"""
        print(sorted(self))
