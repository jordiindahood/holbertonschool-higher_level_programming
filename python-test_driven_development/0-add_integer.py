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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
