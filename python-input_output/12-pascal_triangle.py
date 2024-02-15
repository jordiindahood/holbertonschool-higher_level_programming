#!/usr/bin/python3
"""
    file input-output:
    task 12
"""


def pascal_triangle(n):
    """
    a that defines a student
    public instance attrihbtes:
    first_name -- str
    last_name -- str
    age -- int
    """
    my_list = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        list_cases = [1]
        for j in range(1, i):
            list_cases.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
        list_cases.append(1)
        my_list.append(list_cases)
    return my_list
