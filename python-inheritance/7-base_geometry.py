#!/usr/bin/python3
"""
task 5 file
base_geometry class ??
"""


class BaseGeometry:
    """
    a class
    Attributes: not yet
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
