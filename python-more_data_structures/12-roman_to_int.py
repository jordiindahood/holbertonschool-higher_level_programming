#!/usr/bin/python3
def roman_to_int(roman_string):
    _ro = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    prev = 0

    if isinstance(roman_string, str) or roman_string is None:
        return 0
    for ky in roman_string[::-1]:
        val = _ro[ky]
        if val < prev:
            num -= val
        else:
            num += val
        prev = val
    return num
