import sqlite3
import json


db_loc = 'db/docDB.db'


def execute_select(query):
    conn = sqlite3.connect(db_loc)
    c = conn.cursor()
    c.execute(query)
    res = c.fetchall()
    data = json.dumps(res)
    conn.close()
    return data



def execute_run(query):
    conn = sqlite3.connect(db_loc)
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()
