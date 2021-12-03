import sqlite3 

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO leaderboard (username, score) VALUES (?, ?)",
('JBYT27', 100)) # Example score

connection.commit()
connection.close()