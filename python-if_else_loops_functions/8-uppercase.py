#!/usr/bin/python3
def uppercase(str):
    if not str:
        return
    for letter in str:
        if 'a' <= letter <= 'z':
            letter = chr(ord(letter) - 32)
        print(f"{letter}", end='')
    print()
