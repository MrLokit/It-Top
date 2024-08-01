import sqlite3

conn = sqlite3.connect('26.06.24.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT,
                price REAL,
                quantity INTEGER)''')

products = [
    ('Хлеб', 99.99, 10),
    ('Масло', 159.99, 5),
    ('Сыр', 219.99, 20)
]

cursor.executemany('INSERT INTO products (product_name, price, quantity) VALUES (?, ?, ?)', products)

conn.commit()
conn.close()

print("Таблица 'products' создана и заполнена данными")
