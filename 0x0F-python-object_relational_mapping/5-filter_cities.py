#!/usr/bin/python3

""" Lists all cities of that state, using the database hbtn_0e_4_usa """
import MySQLdb
import sys

if __name__ == '__main__':
    db_connect = MySQLdb.connect(host='localhost',
                                 port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cursor = db_connect.cursor()

    cmd = "SELECT cities.name FROM cities JOIN states ON cities.state_id "
    cmd1 = "= states.id AND states.name = %s ORDER BY cities.id ASC"
    cursor.execute(cmd + cmd1, (sys.argv[4].encode(),))

    results = cursor.fetchall()

    result = ', '.join(city[0] for city in results)
    print(result)

    cursor.close()
    db_connect.close()
