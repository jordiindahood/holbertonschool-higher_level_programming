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
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be > 0")

            if not isinstance(height, int):
                raise TypeError("height must be an integer")
            if height <= 0:
                raise ValueError("height must be > 0")

            if not isinstance(x, int):
                raise TypeError("x must be an integer")
            if x < 0:
                raise ValueError("x must be >= 0")

            if not isinstance(y, int):
                raise TypeError("y must be an integer")
            if y < 0:
                raise ValueError("y must be >= 0")

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
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @x.setter
        def x(self, value):
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @y.setter
        def y(self, value):
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
