#!/usr/bin/python3
"""
    file input-output:
    task 1
"""


def write_file(filename="", text=""):
    """a function that writes the text in a file
    Keyword arguments:
    file_name -- name of file (str), "" if nothing
    text -- text to be written (str), "" if nothing
    Return: none
    """

    words = 0
    with open(filename, "a", encoding="UTF8") as f:
        words += f.write(text)
    f.closed
    return words
