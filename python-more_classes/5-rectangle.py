#!/usr/bin/python3

"""
This script defines a Rectangle class with
properties for width and height,
which are enforced to be positive integers.
"""


class Rectangle:
    """
    Constructor for the Rectangle class,
    initializing a rectangle with the
    given width and height values.
    Defaults to zero if no values are provided.
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """
    Property getter for the height attribute,
    returns the private variable height.
    """

    @property
    def height(self):
        return self.rec_height

    """
    Property setter for the height attribute,
    validating that the input is an
    integer and greater than or equal to 0. Raises a TypeError otherwise.
    """

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.rec_height = value

    """
    Property getter for the width attribute,
    returns the private variable width.
    """

    @property
    def width(self):
        return self.rec_width

    """
    Property setter for the width attribute,
    validating that the input is an
    integer and greater than or equal to 0. Raises a TypeError otherwise.
    """

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.rec_width = value

    def area(self):
        return self.rec_height * self.rec_width

    def perimeter(self):
        if self.rec_height == 0 or self.rec_width == 0:
            return 0
        return (self.rec_height + self.rec_width) * 2

    def __str__(self):
        if self.rec_height != 0 and self.rec_width != 0:
            strr = ("#" * self.rec_width + "\n") * self.rec_height
        else:
            return ""
        return strr[:-1]

    def __repr__(self) -> str:
        return "Rectangle({}, {})".format(self.rec_width, self.rec_height)

    def __del__(self):
        print("Bye rectangle...")
