#!/usr/bin/bash
"""
    holberton-school task 4 module file
"""


def text_indentation(text):
    """
    print a text with 2 new lines after each of these characters:
    ('?', ':','.')
    Parameters:
    - text: str
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    ind = [".", "?", ":"]
    newline_printed = False

    for idx in text:
        if newline_printed and idx.isspace():
            continue

        if idx in ind:
            print(idx + "\n")
            newline_printed = True
        else:
            print(idx, end="")
            newline_printed = False
