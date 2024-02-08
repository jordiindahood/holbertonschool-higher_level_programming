#!/usr/bin/python3
""" holberton-school task 1 module file
"""


def say_my_name(first_name, last_name=""):
    """
    print a sentence that contains {first name} + {last name}

    Parameters:
    - first_name: str
    - last_name: str

    Returns:
    none
    """

    if not type(first_name) is str:
        raise TypeError("first_name must be a string")

    if not type(last_name) is str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
