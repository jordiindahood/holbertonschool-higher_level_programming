#!/usr/bin/python3
plus_plus = __import__('add_0').add
a = 1
b = 2
c = plus_plus(a, b)
print("{} + {} = {}".format(a, b, c))
