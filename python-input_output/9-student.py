#!/usr/bin/python3
"""
    file input-output:
    task 9
"""
class_to_json = __import__("8-class_to_json").class_to_json


class Student:
    """
    a that defines a student
    public instance attrihbtes:
    first_name -- str
    last_name -- str
    age -- int
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return class_to_json(self)
