import sqlite3

# connects to or creates the db
conn = sqlite3.connect('practice.sqlite')
cur = conn.cursor()

# deletes the table if it already exists
cur.execute('DROP TABLE IF EXISTS Ages')

# creates a new table
cur.execute('''
CREATE TABLE Ages (name VARCHAR(128), age INTEGER)''')

# cur.execute('DELETE FROM Ages')
# cur.execute('INSERT INTO Ages (name, age) VALUES ('Obieluem', 29)')
# cur.execute('INSERT INTO Ages (name, age) VALUES ('Valen', 27)')
# cur.execute('INSERT INTO Ages (name, age) VALUES ('Benoit', 40)')
# cur.execute('INSERT INTO Ages (name, age) VALUES ('Callum', 38)')
# cur.execute('INSERT INTO Ages (name, age) VALUES ('Tygan', 24)')
# cur.execute('INSERT INTO Ages (name, age) VALUES ('Sacha', 22)')


conn.commit()

# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#   print(str(row[0]), row[1])

cur.close()