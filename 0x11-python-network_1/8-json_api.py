#!/usr/bin/python3
"""Task 08"""
import requests
import sys

if __name__ == "__main__":
    para = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': para}
    rp = requests.post('http://0.0.0.0:5000/search_user', data)
    json_data = rp.json()
    if len(json_data) == 0:
        print("No result")
    elif 'id' not in json_data.keys() or 'name' not in json_data.keys():
        print("Not a valid JSON")
    else:
        print("[{}] {}".format(json_data.get('id') , json_data.get('name')))

