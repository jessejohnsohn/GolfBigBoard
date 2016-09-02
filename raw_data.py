import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect("golfbigboardTEST.db")
conn.row_factory = dict_factory

c = conn.cursor()

c.execute("select * from golfstratgolfer")

# fetch all or one we'll go for all.

results = str(c.fetchall())

print results

file = open("raw_json.txt", "w")
file.write(results)
file.close()

c.close()
