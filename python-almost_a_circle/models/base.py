#!/usr/bin/python3
"""
    Base class file
"""
import json
import turtle

if __name__ != "__main__":

    class Base:
        """
        Base class file:
        This class will be the “base” of all other classes in this project.
        The goal of it is to manage id attribute in all classes
        and to avoid duplicating the same code (by extension, same bugs)
        """

        __nb_objects = 0

        def __init__(self, id=None):
            if id is not None:
                self.id = id  # just assume that id is an integer in testing
            else:
                Base.__nb_objects += 1
                self.id = self.__nb_objects

        @staticmethod
        def to_json_string(list_dictionaries):
            if list_dictionaries is None:
                return "[]"
            return json.dumps(list_dictionaries)

        @classmethod
        def save_to_file(cls, list_objs):
            """
            that writes the JSON string
            """
            if list_objs is None:
                with open(f"{cls.__name__}.json", "w") as file:
                    json.dump([], file)
            else:
                rep = list(idx.to_dictionary() for idx in list_objs)
                with open(f"{cls.__name__}.json", "w") as file:
                    file.write(cls.to_json_string(rep))

        @staticmethod
        def from_json_string(json_string):
            """that returns the list of the JSON string representation"""
            if json_string is None:
                return []
            return json.loads(json_string)

        @classmethod
        def create(cls, **dictionary):
            """
            a function that returns an instance with all attributes already set
            """
            cls.update(dictionary)
            return cls(**dictionary)

        @classmethod
        def load_from_file(cls):
            """a function that returns a list of instances"""
            try:
                with open(cls.__name__ + ".json", "r") as f:
                    content = cls.from_json_string(f.read())
                    my_list = list()
                    for idx in content:
                        my_list.append(cls.create(**idx))
                    return my_list
            except FileNotFoundError:
                return []

        @staticmethod
        def draw(list_rectangles, list_squares):
            """that opens a window and draws all the Rectangles and Squares"""
            screen = turtle.Screen()
            screen.bgcolor("#6497b1")
            screen.title("python-almost_circle_draw window")
            skk = turtle.Turtle()
            for rec in list_rectangles:
                skk.goto(rec.x + 10, rec.y)
                for idx in range(4):
                    skk.fillcolor("grey")
                    skk.begin_fill()
                    skk.forward(rec.width)
                    skk.left(90)
                    skk.forward(rec.height)
                    skk.left(90)
                    skk.end_fill()
                    skk.hideturtle()
            for sqr in list_squares:
                skk.goto(sqr.x + 10, sqr.y)
                for idx in range(4):
                    skk.fillcolor("grey")
                    skk.begin_fill()
                    skk.forward(sqr.size)
                    skk.left(90)
                    skk.forward(sqr.size)
                    skk.left(90)
                    skk.end_fill()
                    skk.hideturtle()
            turtle.done()
