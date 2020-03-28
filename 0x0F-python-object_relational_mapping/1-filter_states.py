#!/usr/bin/python3
"""Task 01"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset='utf8')
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    data = cursor.fetchall()

    for row in data:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
