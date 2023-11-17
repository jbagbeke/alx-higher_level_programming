#!/usr/bin/python3

""" Lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    if (len(sys.argv) == 4):
        db_connect = MySQLdb.connect(host='localhost', port=3306,  user=sys.argv[1], 
                passwd=sys.argv[2], db=sys.argv[3])

        cursor = db_connect.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id")

        results = cursor.fetchall()

        for result in results:
          print("{}".format(result))

        cursor.close()
        db_connect.close()
