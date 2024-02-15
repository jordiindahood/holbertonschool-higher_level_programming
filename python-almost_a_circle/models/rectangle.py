#!/usr/bin/python3
"""
    Rectangle class file
"""
from . import base


class Rectangle(base.Base):
    """
    ---
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x_axis(self):
        return self.__x

    @x_axis.setter
    def x_axis(self, value):
        self.__x = value

    @property
    def y_axis(self):
        return self.__y

    @y_axis.setter
    def y_axis(self, value):
        self.__y = value
