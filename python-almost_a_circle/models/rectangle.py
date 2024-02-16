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
            """Class init"""
            super().__init__(id)
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y

        # getter/setter : width
        @property
        def width(self):
            return self.__width

        # getter/setter : height
        @property
        def height(self):
            return self.__height

        # getter/setter : x
        @property
        def x(self):
            return self.__x

        # getter/setter : y
        @property
        def y(self):
            return self.__y

        @width.setter
        def width(self, value):
            self.__width = value

        @height.setter
        def height(self, value):
            self.__height = value

        @x.setter
        def x(self, value):
            self.__x = value

        @y.setter
        def y(self, value):
            self.__y = value
