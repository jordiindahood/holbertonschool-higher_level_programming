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
            self.width = width
            self.height = height
            self.x = x
            self.y = y

        # getter/setter : width
        @property
        def fwidth(self):
            return self.width

        @fwidth.setter
        def fwidth(self, value):
            self.width = value

        # getter/setter : height
        @property
        def fheight(self):
            return self.height

        @fheight.setter
        def fheight(self, value):
            self.height = value

        # getter/setter : x
        @property
        def x_axis(self):
            return self.x

        @x_axis.setter
        def x_axis(self, value):
            self.x = value

        # getter/setter : y
        @property
        def y_axis(self):
            return self.y

        @y_axis.setter
        def y_axis(self, value):
            self.y = value
