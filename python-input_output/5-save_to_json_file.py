#!/usr/bin/python3
"""
    file input-output:
    task 3
"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an object to a JSON
    Keyword arguments:
    my_str -- str
    Return: none
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
