#!/usr/bin/python3
"""Define a function ``save_to_json_file``"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text filem using a JSON representation"""
    with open(filename, "w") as line:
        json.dump(my_obj, line)
