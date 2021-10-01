import sqlite3, random
con = sqlite3.connect('example.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS randoms (value int)''')

# Insert a row of data
for i in range(1000):
    cur.execute(f"INSERT INTO randoms VALUES ({random.randint(1, 6)})")

# Save (commit) the changes
con.commit()

res = cur.execute(f"SELECT value, COUNT(value) FROM randoms GROUP BY value;")
print(cur.fetchall())

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()