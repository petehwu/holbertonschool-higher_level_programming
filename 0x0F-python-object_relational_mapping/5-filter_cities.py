#!/usr/bin/python3
""" 0-select_states """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    THE_STATE = argv[4]
    MY_HOST = "localhost"
    MY_PORT = 3306

    db = MySQLdb.connect(host=MY_HOST, port=MY_PORT,
                         user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("""SELECT a.name FROM cities a inner join states b
                   ON a.state_id = b.id
                   WHERE b.name = %s ORDER BY a.id;""", (THE_STATE,))
    rows = cur.fetchall()
    newval = []
    for row in rows:
        newval.append(row[0])
    print(", ".join(newval))
