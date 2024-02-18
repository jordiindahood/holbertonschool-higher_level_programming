#!/usr/bin/python3
"""
    Base class file
"""
import json

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
