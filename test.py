import sqlite3

conn = sqlite3.connect('score.db')

c = conn.cursor()

c.execute("SELECT * FROM score")
print(c.fetchone())

c.close()