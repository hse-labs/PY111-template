import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE writings (writing_id INTEGER PRIMARY KEY AUTOINCREMENT, author, writing )')
conn.close()