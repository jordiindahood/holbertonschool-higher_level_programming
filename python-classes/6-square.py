#!/usr/bin/python3
""" the file for the Square class definition
"""


class Square:
    """a class that creates a square

    Keyword arguments:
    argument -- none
    Return: none
    """

    def __init__(self, size=0, position=(0, 0)):
        self._Square__size = size
        self._Square__pos = position

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

    def my_print(self):
        sig = 0
        if self._Square__pos[1] > 0:
            sig = 1
        if self._Square__size == 0:
            print()
        for line in range(self._Square__size):
            print(" " * self._Square__pos[0], end="")
            for col in range(self._Square__size):
                print("#", end="")
            print()

    @property
    def position(self):
        return self._Square__pos

    @position.setter
    def position(self, value):
        if not isinstance(value[0], int) or isinstance(value[1], int):
            raise Exception("position must be a tuple of 2 positive integers")
        self._Square__pos = value
