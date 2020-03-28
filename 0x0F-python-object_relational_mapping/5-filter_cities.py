#!/usr/bin/python3
"""Task 05"""
import MySQLdb
import sys
import re

if __name__ == "__main__":
    result = []
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities\
        INNER JOIN states ON states.id = cities.id WHERE\
        states.name = %s ORDER BY cities.id ASC", [sys.argv[4]])
    data = cursor.fetchall()

    for row in data:
        result.append(re.search("'(.*)'", (str)(row)).group(1))

    for x in range(len(result)):
        print(result[x], end='')
        if x != len(result) - 1:
            print(", ", end='')
    print()
