#!/usr/bin/python3

""" Displays values in the states table provided name matches the argument """
import MySQLdb
import sys


if __name__ == "__main__":
    db_connect = MySQLdb.connect(host='localhost',
                                 port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cursor = db_connect.cursor()

    cmd = "SELECT * FROM states WHERE name LIKE '%{}%' ".format(sys.argv[4])
    cursor.execute(cmd + "COLLATE utf8mb4_bin ORDER BY states.id ASC")

    values = cursor.fetchall()

    for value in values:
        print("{}".format(value))

    cursor.close()
    db_connect.close()
