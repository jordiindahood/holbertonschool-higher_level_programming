#!/usr/bin/python3
"""sumary_line
Keyword arguments:
argument -- description
Return: return_description
"""


def add_integer(a, b=98):
    """Keyword arguments:
    argument -- a, b
    Return: int"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
