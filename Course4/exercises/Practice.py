# class PartyAnimal:
#   x = 0

#   def party(self):
#     self.x = self.x + 1
#     print("So far", self.x)

# an = PartyAnimal()

# an.party()
# an.party()
# an.party()
# an.party()
# an.party()
# an.party()

import sqlite3

# connects to or creates the db
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# deletes the table if it already exists
cur.execute('DROP TABLE IF EXISTS Counts')

# creates a new table
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
  if not line.startswith('From: '):
    continue
  pieces = line.split()
  email = pieces[1]
  cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
  row = cur.fetchone()
  if row is None:
    cur.execute('''INSERT INTO Counts (email, count)
    VALUES (?, 1)''', (email,))
  else:
    cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
  conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
  print(str(row[0]), row[1])

cur.close()