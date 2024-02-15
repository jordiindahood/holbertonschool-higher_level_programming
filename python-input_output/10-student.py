#!/usr/bin/python3
"""
    file input-output:
    task 10
"""


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

    def to_json(self, attrs=None):
        """retrieve a dictionary representation of student"""
        if attrs is None:
            return self.__dict__
        else:
            dikt = dict()
            for idx in attrs:
                if idx in self.__dict__.keys():
                    dikt.update(dict(idx=self.__dict__[idx]))
            return dikt
