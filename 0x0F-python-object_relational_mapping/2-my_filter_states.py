#!/usr/bin/python3
"""Task 02"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
            (sys.argv[4],))
    data = cursor.fetchall()

    for row in data:
        print(row)
