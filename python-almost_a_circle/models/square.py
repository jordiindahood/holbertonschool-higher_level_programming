#!/urs/bin/python3
"""
    Square class file
"""
from .rectangle import Rectangle

if __name__ != "__main__":

    class Square(Rectangle):
        """
        Rectangle: a class that inherited from Base class
        width: int
        height: int
        x,y: int
        id: int , None if not assigned
        """

        def __init__(self, size, x=0, y=0, id=None):
            """Class init"""
            super().__init__(size, size, x, y, id)

        def __str__(self):
            S_str = str(
                f"[Square] ({self.id}) {self.x}/{self.y}" +
                f" - {self.width}"
            )
            return S_str
