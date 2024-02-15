#!/usr/bin/python3
"""
    Base class file
"""


class Base:
    """
    class---
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id  # just assume that id is an integer in testing
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
