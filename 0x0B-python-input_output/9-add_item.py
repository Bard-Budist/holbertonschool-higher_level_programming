#!/usr/bin/python3
import sys
import os.path
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

data = []
if os.path.isfile("add_item.json"):
    save_to_json_file(data, "add_item.json")
    data = load_from_json_file("add_item.json")
    for items in sys.argv[1:]:
        data.append(items)
    save_to_json_file(data, "add_item.json")
else:
    with open("add_item.json", mode="w+") as file:
        file.write(str(data))
