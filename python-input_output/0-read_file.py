#!/usr/bin/python3
"""
    file input-output:
    task 0 
"""


def read_file(filename=""):
    """a function that reads a file
    Keyword arguments:
    file_name -- name of file (str), "" if nothing
    Return: none
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
    f.closed
