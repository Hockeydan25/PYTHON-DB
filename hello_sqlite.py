import sqlite3

conn = sqlite3.connect('first_db.sqlite')  #connect ot create new if doesn't exist.

conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')  
# need to have:IF NOT EXISTS for tables and DB's.

# THIS WILL keep creating if you re-reun
# conn.execute('INSERT INTO products VALUES (1000, "hat")' )
# conn.execute('INSERT INTO products VALUES (1001, "tshirt")')

conn.commit()  # don't forget!

results = conn.execute('SELECT * FROM products')

# for row in results:  # this was writen in first video.
#     print(row)  # each row return is a tuple.


first_row = results.fetchone()  # written is second video. 
print(first_row) 

new_id = int(input('enter new id: '))
new_name = input('enter new product: ')

# no format strings {new_id} use paramerized value queries, sql statement.
#conn.execute(f'INSERT INTO products VALUES (?, ?)', (new_id, new_name) )
#conn.commit()  # don't forget this commit line.

# update_product = 'wool hat'
# update_id = 1000
# conn.execute('UPDATE products SET name = ? WHERE id = ?', (update_product, update_id) )
# # does it matter the order here?
# conn.commit() 

delete_product = '"'
conn.execute('DELETE FROM products WHERE name = ?', (delete_product, ) )
# does it matter the order here?
conn.commit() 

conn.close()