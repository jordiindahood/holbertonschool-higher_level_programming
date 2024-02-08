#!/usr/bin/python3
""" holberton-school task 1 module file
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by the specified divisor.

    Parameters:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor.

    Returns:
    - new_matrix (list of lists): The resulting matrix after division.
    """

    for lis in matrix:
        if len(matrix[0]) != len(lis):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in lis:
            if not type(elem) in [int, float]:
                raise TypeError(
                    "matrix must be a matrix " + "(list of lists) of integers/floats"
                )
    if not type(div) in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
    return new_matrix
