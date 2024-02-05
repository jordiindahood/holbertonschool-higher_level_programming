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
        if not isinstance(size, int):
            raise Exception("size must be an integer")
        if size < 0:
            raise Exception("size must be >= 0")
        self._Square__size = size
        pass
    def area(self):
        return self._Square__size ** 2
