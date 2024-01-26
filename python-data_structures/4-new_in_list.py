#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if my_list and -1 < idx < len(my_list) and element:
        new_list[idx] = element
    return new_list
