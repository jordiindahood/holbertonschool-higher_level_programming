#!/usr/bin/python3
"""
    Inheritance: module file
"""
def lookup(obj):
    """
        lookup: a function that returns a list
        containing available attributes and methods 
        of an object {obj}
    """
    return dir(obj)
