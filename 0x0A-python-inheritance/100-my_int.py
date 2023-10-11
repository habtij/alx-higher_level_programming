#!/usr/bin/python3
"""Defines a class ``MyInt`` that inherits from ``int``"""


class MyInt(int):
    """represents MyInt"""
    def __eq__(self, value):
        """Override `==` with `!=` behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override `!=` with `==` behavior"""
        return self.real == value
