#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    connect to the database and select list of states in database
    """
    data_connect = MySQLdb.connect(host="localhost",
                                   port=3306,
                                   user=sys.argv[1],
                                   passwd=sys.argv[2],
                                   db=sys.argv[3])
    cur = data_connect.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id;")
    cur = cur.fetchall()
    for row in cur:
        print(row)
    cur.close()
    data_connect.close()
