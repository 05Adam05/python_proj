import sqlite3

conn = sqlite3.connect("class.db")
bd_cur = conn.cursor()

bd_cur.execute("DROP TABLE class")


bd_cur.execute("""CREATE TABLE class (
	name VARCHAR(20) PRIMARY KEY,
	studies VARCHAR(20),
	iq REAL
)""")

bd_cur.execute("INSERT INTO class VALUES('Адам', 'учеба отлично', 100)")
bd_cur.execute("INSERT INTO class VALUES('Камиль', 'Хоршо', 80) ")

# bd_cur.execute("INSERT INTO class VALUES(?,?,?,?)", ("Султанмурад", "Silver", 1.5, "QBZ95"))
ins = "INSERT INTO class VALUES(?,?,?)"
data = "Султанмурад", "Плохо", 50
bd_cur.execute(ins, data)

conn.commit()

bd_cur.close()
conn.close()