#!/usr/bin/python3
"""Defines a function ``read_file``"""


def read_file(filename=""):
    """reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as line:
        print(line.read(), end="")
