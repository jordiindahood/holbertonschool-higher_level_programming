#!/usr/bin/python3
def read_file(file_name=""):
    with open(file_name, encoding="utf-8") as f:
        print(f.read())
    f.closed
