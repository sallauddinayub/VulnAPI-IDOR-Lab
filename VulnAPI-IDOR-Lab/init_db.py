import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    balance INTEGER
)
''')

users = [
    (1, "Rahul", "rahul@gmail.com", 12450),
    (2, "Priya", "priya@gmail.com", 87000),
    (3, "Amit", "amit@gmail.com", 5420),
    (4, "Sara", "sara@gmail.com", 33000),
    (5, "Vikram", "vikram@gmail.com", 9100),
]

c.executemany("INSERT OR REPLACE INTO users VALUES (?, ?, ?, ?)", users)

conn.commit()
conn.close()

print("Database initialized with sample users.")
