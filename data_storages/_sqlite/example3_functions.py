import sqlite3


def upper_word(raw):
    return raw.upper()


conn = sqlite3.connect(':memory:')
conn.create_function('upper_func', 1, upper_word)
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS users(first_name char(20))')
cur.execute(
    'INSERT INTO users(first_name) VALUES ("Eugene"),("Dmitry"),("Viktor")'
)
cur.execute('SELECT upper_func(first_name) FROM users')
row = cur.fetchone()
print(row)
