import sqlite3

#vaildation errors, rowid

db = 'products.sqlite'  # why not a if not exists here?

with sqlite3.connect(db) as conn:  # watch the pairs of ()
    conn.execute('CREATE TABLE IF NOT EXISTS products (name TEXT UNIQUE, quantity INT)')
conn.close()

name = 'blanket'
quantity = 2

try:
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products (name, quantity) VAlUES (?, ?)', (name, quantity) )
    conn.close()
except Exception as e:
     print('Error inserting ', e)

conn = sqlite3.connect(db)
results = conn.execute('SELECT * FROM products')

for row in results:
    print(row)

print('end of program!')



