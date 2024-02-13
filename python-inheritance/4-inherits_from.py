#!/usr/bin/python3
"""
task 3 file
4-inherits_from.py ??
"""


def inherits_from(obj, a_class):
    """
    obj: obj
    a_class: class
    return true if type(obj) is a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
