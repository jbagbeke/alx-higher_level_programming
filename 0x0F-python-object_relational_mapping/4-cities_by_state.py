#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys

if __name__ == '__main__':
    if (len(sys.argv) == 4):
        db_connect = MySQLdb.connect(host='localhost',
                                     port=3306,
                                     user=sys.argv[1],
                                     passwd=sys.argv[2],
                                     db=sys.argv[3])
        cursor = db_connect.cursor()
        cmd = "SELECT * FROM cities JOIN states ON cities.state_id = states.id"
        cursor.execute(cmd + " ORDER BY cities.id ASC")

        results = cursor.fetchall()

        for result in results:
            print("{}".format(result))

        cursor.close()
        db_connect.close()
