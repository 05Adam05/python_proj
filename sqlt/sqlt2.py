import sqlite3

conn = sqlite3.connect("class.db")
bd_cur = conn.cursor()

bd_cur.execute("SELECT * FROM class")
info = bd_cur.fetchall()
print(info)

conn.commit()

bd_cur.close()
conn.close()