#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    res = 0
    for index in range(1, len(argv)):
        res += int(argv[index])
    print("{}".format(res))
