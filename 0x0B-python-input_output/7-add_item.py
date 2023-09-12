#!/usr/bin/python3
"""
A script that adds all arguments to a Python list
"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    jba_list = []
    with open("add_item.json", "w", encoding="UTF-8") as file:
        json.dump(jba_list, file)
else:
    for i in range(len(sys.argv) - 1):
        my_list.append(sys.argv[i + 1])
save_to_json_file(my_list, "add_item.json")
