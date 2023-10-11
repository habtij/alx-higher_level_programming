#!/usr/bin/python3
"""Defines a function ``append_write``"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file and returns the number of
    characters
    """
    with open(filename, "a", encoding="utf-8") as line:
        return file.write(text)
