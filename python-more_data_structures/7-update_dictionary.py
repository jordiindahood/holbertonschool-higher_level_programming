#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    signal = 0
    for k in a_dictionary:
        if key == k:
            signal = 1
            break
    if signal == 1:
        a_dictionary.setdefault(str(key), value)
    else:
        a_dictionary.update({str(key): value})
    return a_dictionary
