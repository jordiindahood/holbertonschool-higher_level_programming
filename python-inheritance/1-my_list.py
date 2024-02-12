#!/usr/bin/python3
"""
    A subclass of list that provides a method to
    print a sorted version of itself.
"""


class MyList(list):
    """a subclass of List

    Keyword arguments:
    argument -- description
    Return: None
    """

    def print_sorted(self):
        """
        ########################################
        #Prints the sorted version of the list.#
        ########################################
        """
        print(sorted(self))
