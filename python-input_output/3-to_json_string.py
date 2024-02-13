#!/usr/bin/python3
"""
    file input-output:
    task 3
"""
import json


def to_json_string(my_obj):
    """a function that writes the text in a file
    Keyword arguments:
    file_name -- name of file (str), "" if nothing
    text -- text to be written (str), "" if nothing
    Return: none
    """

    return json.dumps(my_obj)
