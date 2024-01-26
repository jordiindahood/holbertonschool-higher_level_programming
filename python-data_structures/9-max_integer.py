#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = None
    if my_list is not None:
        maxi = my_list[0]
        for idx in my_list:
            if idx is not None and maxi < idx:
                maxi = idx
    return maxi
