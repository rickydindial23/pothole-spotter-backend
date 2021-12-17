import sqlite3

with sqlite3.connect("SignUp.db") as db:
    cursor = db.cursor()

cursor.execute( '''
CREATE TABLE IF NOT EXISTS user(
First Name 
Last Name 
Username
Email
Password
)

''')