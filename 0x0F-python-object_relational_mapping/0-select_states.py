#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """
    connect to the database and select list of states in database
    """
    conection = MySQLdb.connect(host="localhost", port=3306,
                               password=argv[2], user=argv[1],
                               db = argv[3])
    cur = conection.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    for states in cur.fetchall():
        print(states)
    cur.close()
    conection.close()
