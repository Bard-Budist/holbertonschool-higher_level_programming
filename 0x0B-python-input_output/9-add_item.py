#!/usr/bin/python3
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

data = []
if (len(sys.argv) == 1):
    save_to_json_file(data, "add_item.json")
else:
    data = load_from_json_file("add_item.json")
    for items in sys.argv[1:]:
        data.append(items)
    save_to_json_file(data, "add_item.json")
