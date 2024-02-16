#!/usr/bin/python3
"""
    Square class file
"""
from .rectangle import Rectangle

if __name__ != "__main__":

    class Square(Rectangle):
        """
        Rectangle: a class that inherited from Base class
        size: int
        x,y: int , 0 if not assigned
        id: int , None if not assigned
        """

        def __init__(self, size, x=0, y=0, id=None):
            """Class init"""
            super().__init__(size, size, x, y, id)

        def __str__(self):
            """string representation of Square class"""
            S_str = str(f"[Square] ({self.id}) {self.x}/{self.y}" + f" - {self.width}")
            return S_str

        @property
        def size(self):
            return self.width

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.width = value

        def update(self, *args, **kwargs):
            """
            update():
            update the class Rectangle
            """

            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

            for ky, vl in kwargs.items():
                setattr(self, ky, vl)

        def to_dictionary(self):
            """to_dictionary():
            this function prints the dictionary representation
            of Square class
            """
            new_dict = dict()
            new_dict.update({"id": self.id})
            new_dict.update({"x": self.x})
            new_dict.update({"size": self.width})
            new_dict.update({"y": self.y})
            return new_dict
