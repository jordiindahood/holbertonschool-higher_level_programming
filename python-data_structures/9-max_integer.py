#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = None
    if my_list is not None:
        for num in my_list:
            if num is not None:
                maxi = num
    for idx in my_list:
        if idx is None:
            continue
        if maxi < idx:
            maxi = idx
    return maxi
