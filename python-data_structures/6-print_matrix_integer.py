#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for vec in range(len(matrix)):
        for idx in range(len(matrix[vec])):
            print("{:d}".format(matrix[vec][idx]), end="")
            if idx < 2:
                print(end=" ")
        print()
