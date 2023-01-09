import sqlite3

con = sqlite3.connect('./test.db')

cur = con.cursor()

cur.execute("select * from sqlite_master;")
print(cur.fetchall())

try:
    cur.execute("CREATE TABLE resource_summary(time INTEGER," + 
                "cpu INTEGER, mem INTEGER, temperature INTEGER);")
except Exception as e:
    print(e)

dataList = ((0,1,2,3), (1,2,3,4), (2,3,4,5))

cur.executemany("INSERT INTO resource_summary VALUES(?, ?, ?, ?);", dataList)

cur.execute('SELECT * FROM resource_summary')
for row in cur:
    print(row)

cur.fetchone()

cur.fetchmany(2)

cur.fetchall()
