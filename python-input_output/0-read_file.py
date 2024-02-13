#!/usr/bin/python3
"""
    file input-output: task 0 
"""
def read_file(file_name=""):
    """a function that reads a file

    Keyword arguments:
    file_name -- name of file (str), "" if nothing
    Return: none
    """
    
    with open(file_name) as f:
        print(f.read())
    f.closed
