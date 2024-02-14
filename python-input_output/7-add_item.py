#!/usr/bin/python3
"""
    file input-output:
    task 7
"""
from sys import argv
from os.path import isfile

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file = "add_item.json"

if isfile(file):
    data = load_from_json_file(file)
else:
    data = []
save_to_json_file(list(data + argv[1:]), file)
