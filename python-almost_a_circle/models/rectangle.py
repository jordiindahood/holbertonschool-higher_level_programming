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
            if True:
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
            # initialization
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

        def area(self):
            """
            area():
            this function returns the area of a rectangle
            """
            return self.__height * self.__width

        def __str__(self):
            R_str = str(
                f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                + f" - {self.__width}/{self.__height}"
            )
            return R_str

        def display(self):
            """
            display():
            this function prints the rectangle with # character
            """
            the_form = self.__y * "\n" + (
                (self.__x * " " + "#" * self.__width + "\n") * self.__height
            )
            print(the_form[:-1])

        def update(self, *args, **kwargs):
            """
            update():
            update the class Rectangle
            """

            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                if not isinstance(args[1], int):
                    raise TypeError("width must be an integer")
                if args[1] <= 0:
                    raise ValueError("width must be > 0")
                self.__width = args[1]
            if len(args) > 2:
                if not isinstance(args[2], int):
                    raise TypeError("height must be an integer")
                if args[2] <= 0:
                    raise ValueError("height must be > 0")
                self.__height = args[2]
            if len(args) > 3:
                if not isinstance(args[3], int):
                    raise TypeError("x must be an integer")
                if args[3] < 0:
                    raise ValueError("x must be >= 0")
                self.__x = args[3]
            if len(args) > 4:
                if not isinstance(args[4], int):
                    raise TypeError("y must be an integer")
                if args[4] < 0:
                    raise ValueError("y must be >= 0")
                self.__y = args[4]

            for ky, vl in kwargs.items():
                setattr(self, ky, vl)

        def to_dictionary(self):
            """to_dictionary():
            this function printsthe dictionary representation
            of Rectangle class
            """
            new_dict = dict()
            new_dict.update({"x": self.__x})
            new_dict.update({"y": self.__y})
            new_dict.update({"id": self.id})
            new_dict.update({"height": self.__height})
            new_dict.update({"width": self.__width})
            return new_dict
