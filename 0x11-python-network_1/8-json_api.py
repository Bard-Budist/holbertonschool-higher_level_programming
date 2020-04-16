#!/usr/bin/python3
"""Task 08"""
import requests
import sys

if __name__ == "__main__":
    para = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': para}
    rp = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        json_data = rp.json()
    except Exception as err:
        print("Not a valid JSON")
    if len(json_data) == 0:
        print("No result")
    else:
        print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
