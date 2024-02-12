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

    # public instance
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            sy = self.print_symbol
            strr = (str(sy) * self.rec_width + "\n") * self.rec_height
        else:
            return ""
        return strr[:-1]

    def __repr__(self) -> str:
        return "Rectangle({}, {})".format(self.rec_width, self.rec_height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Make a square from a rectangle
        Args:
            size (int): the size of the square
        Returns:
            (Rectangle): instance of rectangle
        """
        return cls(size, size)
