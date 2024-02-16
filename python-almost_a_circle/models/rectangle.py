#!/usr/bin/python3
"""
    Rectangle class file
"""
from .base import Base

if __name__ != "__main__":

    class Rectangle(Base):
        """
        Rectangle: a class that inherited from Base class
        width: int
        height: int
        x,y: int
        id: int , None if not assigned
        """

        def __init__(self, width, height, x=0, y=0, id=None):
            super().__init__(id)
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y

        # getter/setter : width
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        # getter/setter : height
        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        # getter/setter : x
        @property
        def x_axis(self):
            return self.__x

        @x_axis.setter
        def x_axis(self, value):
            self.__x = value

        # getter/setter : y
        @property
        def y_axis(self):
            return self.__y

        @y_axis.setter
        def y_axis(self, value):
            self.__y = value
