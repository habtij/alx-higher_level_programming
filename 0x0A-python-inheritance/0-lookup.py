#!/usr/bin/python3

def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return (list(obj.__dict__))
