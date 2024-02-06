#!/usr/bin/python3
""" the file for the Square class definition
"""


class Square:
    """a class that creates a square

    Keyword arguments:
    argument -- none
    Return: none
    """

    def __init__(self, size=0):
        self._Square__size = size

    def area(self):
        return self._Square__size**2

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise Exception("size must be an integer")
        if value < 0:
            raise Exception("size must be >= 0")
        self._Square__size = value
