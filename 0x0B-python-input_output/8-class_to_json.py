#!/usr/bin/python3
"""Defines a function ``class_to_json``"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return obj.__dict__
