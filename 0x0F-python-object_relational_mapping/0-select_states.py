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
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2], database=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    database.close()
