#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = list()
    try:
        for idx in range(list_length):
            try:
                new_list.append(my_list_1[idx] / my_list_2[idx])
            except IndexError:
                print("out of range")
                new_list.append(0)
            except TypeError:
                new_list.append(0)
                print("wrong type")
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
    finally:
        return new_list
