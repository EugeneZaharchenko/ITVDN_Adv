import sqlite3

conn = sqlite3.connect('repr_db.sqlite3')
conn.execute(
    """CREATE TABLE IF NOT EXISTS "users" (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           first_name,
           last_name,
           birthday
   )""")
conn.execute("""
        insert into users(id, first_name, last_name, birthday)
        VALUES (1, "Eugene", "Hatsko", "09-11-1992"),
               (2, "Dmitry", "Ivanov", "01-09-1993")
   """)
conn.commit()

conn.row_factory = sqlite3.Row
users = conn.execute('SELECT * FROM "users"').fetchall()

user = users[0]
print(user.keys())
print(user['id'], user['iD'])
print(user['first_name'], user['first_NAME'], user['FIRST_NAME'])
