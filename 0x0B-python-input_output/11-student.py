#!/usr/bin/python3
"""Define a class ``Student`` in ``10-student`` module"""


class Student:
    """represents a student object"""
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) == list and all(type(ele) == str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self. json):
        """replaces all attributes of the ``Student`` instance"""
        for key, value in json.items():
            setattr(self, key, value)
