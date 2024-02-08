#!/usr/bin/python3
""" holberton-school task 1 module file
Keyword arguments:
argument -- description
Return: return_description
"""


def matrix_divided(matrix, div):
    """Keyword arguments:
    argument -- a, b
    Return: int"""
    for lis in matrix:
        if len(matrix[0]) != len(lis):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in lis:
            if not type(elem) in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
    if not type(div) in [int, float]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x/div,2), i)))
    return new_matrix
