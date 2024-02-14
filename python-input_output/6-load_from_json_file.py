#!/usr/bin/python3
"""
    file input-output:
    task 6
"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON
    Keyword arguments:
    my_str -- str
    Return: none
    """
    with open(filename, "r") as f:
        return json.load(f)
