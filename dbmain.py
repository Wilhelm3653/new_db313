import sqlite3

connection = sqlite3.connect('database/db.db')
cursor = connection.cursor()

# connection.cursor().execute('''
#     CREATE TABLE IF NOT EXISTS Users (
#     id INTEGER PRIMARY KEY,
#     UserName TEXT NOT NULL        
#                             )
# ''')

# connection.cursor().execute('INSERT INTO Users (id, UserName) VALUES (?, ?)', (1, 'newuser'))

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

for user in users:
  print(user)

connection.commit()
connection.close()