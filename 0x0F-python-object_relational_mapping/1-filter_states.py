#!/usr/bin/python3

""" Lsts all states with a name starting with N (upper N) from a database """
import MySQLdb
import sys

if __name__ == "__main__":
    db_connect = MySQLdb.connect(host='localhost',
                                 port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cursor = db_connect.cursor()
    cmd1 = "COLLATE utf8mb4_bin ORDER BY states.id ASC"
    cmd = "SELECT * FROM states WHERE name LIKE 'N%' " + cmd1
    cursor.execute(cmd)

    names = cursor.fetchall()

    for name in names:
        print("{}".format(name))

    cursor.close()
    db_connect.close()
