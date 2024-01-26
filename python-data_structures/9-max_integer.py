#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != None:
        maxi = my_list[0]
        for idx in my_list:
            if maxi < idx:
                maxi = idx
        return maxi
    return None