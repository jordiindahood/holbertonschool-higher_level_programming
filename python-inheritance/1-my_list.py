#!/usr/bin/python3
"""
        Inheritance: module file
"""


class MyList(list):
    """
    a subclass of List
    """

    def print_sorted(self):
        """
        print a sorted version
        """
        print(sorted(self))
