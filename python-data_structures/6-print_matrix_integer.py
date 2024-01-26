#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for vec in range(len(matrix)):
        for idx in range(len(matrix[vec])):
            print("{}".format(matrix[vec][idx]), end="")
            if idx < 3:
                print(end=" ")
        print()
