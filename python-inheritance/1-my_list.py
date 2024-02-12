#!/usr/bin/python3
"""
        Inheritance: module file
"""


class MyList(list):
    """
    inherit the list Class to MyList class
    """

    def print_sorted(self):
        print(sorted(self))
