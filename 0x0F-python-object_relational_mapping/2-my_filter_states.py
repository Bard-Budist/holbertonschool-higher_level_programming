#!/usr/bin/python3
"""Task 02"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    data = cursor.fetchall()

    for row in data:
        if row[1] == sys.argv[4]:
            print(row)
    cursor.close()
    db.close()
