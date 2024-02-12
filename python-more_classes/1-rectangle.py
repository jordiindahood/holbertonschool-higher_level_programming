#!/usr/bin/python3

"""
    This class creates a rectangle
    width: int
    height: int
"""


class Rectangle:
    """
    Rectangle: a class that creates a rectangle
    Default: zero if width or height not assigned
    """

    def __init__(self, width=0, height=0):
        self.__rectangle__height = int(height)
        self.__rectangle__width = int(width)

    """
    Proprety: getter to the height attribute
    """

    @property
    def height(self):
        return self.__rectangle__height

    """
    Proprety: setter for the height attribute
    height should be an integer and >= than zero
    """

    @height.setter
    def height(self, value):
        if type(value) is not (int or bool):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__rectangle__height = int(value)

    """
    Proprety: getter to the width attribute
    """

    @property
    def width(self):
        return self.__rectangle__width

    """
    Proprety: getter to the width attribute
    width should be an integer and >= than zero
    """

    @width.setter
    def width(self, value):
        if type(value) is not (int or bool):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__rectangle__width = int(value)
