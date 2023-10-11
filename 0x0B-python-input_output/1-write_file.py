#!/usr/bin/python3
"""Defines a function ``write_file``"""


def write_file(filename="", text=""):
    """Write a string to a text file and returns the number character"""
    with open(filename, "w", encoding="utf-8") as line:
        return line.write(text)
