import sqlite3

db = 'first_db.sqlite'

def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')  
    #need to have:IF NOT EXISTS for tables and DB's.
    conn.close()


def insert_example_data():
    with sqlite3.connect(db) as conn:
    #THIS WILL keep creating if you re-reun
        conn.execute('INSERT INTO products VALUES (1000, "hat")' )
        conn.execute('INSERT INTO products VALUES (1001, "jacket")')
    conn.close()    
   

def display_all_data():  
    conn = sqlite3.connect(db) 
    results = conn.execute('SELECT * FROM products')
    print('All Products: ')
    for row in results:  # this was writen in first video.
        print(row)  # each row return is a tuple.
    conn.close()    


def display_one_product(product_name):
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products WHERE name like ?', (product_name, ))
    first_row = results.fetchone()
    if first_row:
        print('Your product is: ', first_row)
    else:
        print('not found in database')     
    conn.close()


def create_new_product():
    new_id = int(input('enter new id: '))
    new_name = input('enter new product: ')
    # no format strings {new_id} use paramerized value queries, sql statement.
    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO products VALUES (?, ?)', (new_id, new_name) )
    conn.close()


def update_product():
    conn = sqlite3.connect(db)
    update_product = 'wool hat'
    update_id = 1000
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE products SET name = ? WHERE id = ?', (update_product, update_id) )
    # # does it matter the order here?
    conn.close()
    

def delete_product(product_name):
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE FROM products WHERE name = ?', (product_name, ) )
    # does it matter the order here?
    conn.close()

create_table()
insert_example_data()
display_all_data()
display_one_product('jacket')
display_one_product('coat')
create_new_product()
update_product()
delete_product('jacket')
display_all_data()