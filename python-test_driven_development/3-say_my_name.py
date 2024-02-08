#!/usr/bin/python3
""" holberton-school task 1 module file
"""


def say_my_name(first_name, last_name=""):
    """
    Divides all elements of a matrix by the specified divisor.

    Parameters:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor.

    Returns:
    - new_matrix (list of lists): The resulting matrix after division.
    """

    if not type(first_name) is str:
        raise TypeError("first_name must be a string")

    if not type(last_name) is str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
