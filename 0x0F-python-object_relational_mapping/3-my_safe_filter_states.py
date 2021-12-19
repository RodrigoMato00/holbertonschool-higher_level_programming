#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    """
    connect to the database and select list of states in database
    """
    import MySQLdb
    import sys

    data_connect = MySQLdb.connect(host="localhost",
                                   port=3306,
                                   user=sys.argv[1],
                                   passwd=sys.argv[2],
                                   db=sys.argv[3])
    cur = data_connect.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name=%s ORDER BY id ASC",
                (argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    data_connect.close()