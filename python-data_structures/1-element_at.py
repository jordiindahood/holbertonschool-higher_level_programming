#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or not my_list:
        return
    if idx < len(my_list):
        return my_list[idx]
    return
