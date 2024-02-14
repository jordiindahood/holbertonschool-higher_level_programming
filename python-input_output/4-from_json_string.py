#!/usr/bin/python3
"""
    file input-output:
    task 3
"""
import json


def from_json_string(my_str):
    """a function that returns object from a JSON
    Keyword arguments:
    my_str -- str
    Return: none
    """
    return json.loads(my_str)
