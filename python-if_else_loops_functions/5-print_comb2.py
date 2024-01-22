#!/usr/bin/python3
for num in range(100):
    if num < 99:
        print("%02d" % num, end=", ")
    else:
        print("%02d" % num)
