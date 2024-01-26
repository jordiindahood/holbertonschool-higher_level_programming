#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    idx = 0
    count = 0
    while count != length:
        print("{}".format(my_list[length - 1 - idx]))
        idx = idx + 1
        count = count + 1
