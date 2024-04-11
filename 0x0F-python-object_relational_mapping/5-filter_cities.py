#!/usr/bin/python3
""" This script lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    databaseName = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost', user=username, passwd=password, db=databaseName
        )
    cur = db.cursor()
    try:
        cur.execute("""SELECT c.name FROM cities AS c
                    INNER JOIN states AS s
                    ON state_id = s.id
                    WHERE s.name = %s
                    ORDER BY c.id""", (state_name, ))
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        try:
            print(f"MySQL Error [{e.args[0]}]: {e.args[1]}")
        except IndexError:
            print(f"MySQL Error: {str(e)}")
    cities = []
    for row in rows:
        cities.append(row[0])
    print(*cities, sep=", ")
    cur.close()
    db.close()
