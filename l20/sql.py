import sqlite3

conn = sqlite3.connect("csgamers.db")
bd_cur = conn.cursor()

bd_cur.execute("DROP TABLE cs_gamers")

bd_cur.execute("""CREATE TABLE cs_gamers (
	name VARCHAR(16) PRIMARY KEY,
	rating VARCHAR(20),
	stats REAL,
	top_gun VARCHAR(30)
)""")

bd_cur.execute("INSERT INTO cs_gamers VALUES('Адам', 'Global Elite', 1.8, 'Керамбит Кровавая паутина')")
bd_cur.execute("INSERT INTO cs_gamers VALUES('Камиль', 'Беркут', 1.6, 'Драгонлор') ")

# bd_cur.execute("INSERT INTO cs_gamers VALUES(?,?,?,?)", ("Султанмурад", "Silver", 1.5, "QBZ95"))
ins = "INSERT INTO cs_gamers VALUES(?,?,?,?)"
data = "Султанмурад", "Silver", 1.5, "QBZ95"
bd_cur.execute(ins, data)

conn.commit()

bd_cur.close()
conn.close()