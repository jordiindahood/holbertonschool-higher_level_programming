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
            return super().update(*args, **kwargs)