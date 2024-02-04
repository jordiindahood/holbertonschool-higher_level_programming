#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    case_num = 0
    try:
        for idx in range(x):
            print("{}".format(my_list[idx]), end="")
            case_num += 1
    except:
        print()
    return case_num
