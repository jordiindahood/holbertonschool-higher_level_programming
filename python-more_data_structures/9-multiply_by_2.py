#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict()
    for ky, vl in a_dictionary.items():
        x = vl * 2
        new_dict.update({str(ky): x})
    return new_dict
