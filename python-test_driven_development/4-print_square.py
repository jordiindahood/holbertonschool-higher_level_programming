#!/usr/bin/python3
""" holberton-school task 3 module file
"""


def print_square(size):
    """
    draw a square with '#' depending on size
    Parameters:
    - size: int
    """
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    line = str("#" * size) + "\n"
    print(line * size)
