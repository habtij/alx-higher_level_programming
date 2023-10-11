#!/usr/bin/python3
"""Define a function ``load_from_json_file``"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename) as line:
        return json.load(line)
