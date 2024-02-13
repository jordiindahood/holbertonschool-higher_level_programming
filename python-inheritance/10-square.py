#!/usr/bin/python3
"""
task 10 file
Square class ??
"""

rec = __import__("9-rectangle").Rectangle


class Square(rec):
    """
    a class based on BaseGeometry class
    Attributes: not yet
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
