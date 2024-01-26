#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    frst_elm = tuple_a[0] + tuple_b[0]
    scnd_elm = tuple_a[1] + tuple_b[1]
    new_tuple = (frst_elm, scnd_elm)

    return new_tuple
