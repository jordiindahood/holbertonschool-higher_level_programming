#!/usr/bin/python3
"""
    This class creates a rectangle
"""


class Rectangle:
    """
    Rectangle: a class that creates a rectangle
    """

    def __init__(self, width=0, height=0):
        """INITIALIZE the rectangle with a height and width"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__rectangle__height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__rectangle__width = width

    """Proprety: getter to the height attribute"""

    @property
    def height(self):
        return self.__rectangle__height

    """Proprety: setter for the height attribute"""

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__rectangle__height = value

    """Proprety: getter to the width attribute"""

    @property
    def width(self):
        return self.__rectangle__width

    """Proprety: getter to the width attribute"""

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__rectangle__width = value
