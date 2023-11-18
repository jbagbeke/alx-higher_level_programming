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
    cmd = "SELECT * FROM states WHERE name LIKE %s "
    cmd1 = "COLLATE utf8mb4_bin ORDER BY states.id ASC"
    cursor.execute(cmd + cmd1, (('%' + sys.argv[4] + '%').encode(),))

    values = cursor.fetchall()

    for value in values:
        print("{}".format(value))

    cursor.close()
    db_connect.close()
