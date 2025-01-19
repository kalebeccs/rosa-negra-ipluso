import sqlite3
import users


from data import USERS, WINES, STOCK, PURCHASES, PURCHASE_ITEMS

conn = sqlite3.connect('rosa_negra.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    pk_user INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dob DATE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    vat_number INTEGER,
    address_1 TEXT,
    address_2 TEXT,
    role TEXT NOT NULL
)             
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS wines(
    pk_wine INTEGER PRIMARY KEY,
    brand TEXT NOT NULL, 
    name TEXT NOT NULL,
    price REAL NOT NULL,
    type TEXT NOT NULL,
    alcohol REAL NOT NULL,
    year INTEGER NOT NULL,
    region TEXT NOT NULL,
    description TEXT NOT NULL
)            
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS stocks(
    pk_stock INTEGER PRIMARY KEY,
    fk_wine INTEGER NOT NULL,
    movement TEXT CHECK(movement IN ('purchase', 'sale', 'adjustment')) NOT NULL,
    quantity INTEGER NOT NULL,
    fk_user INTEGER,
    reason TEXT,
    FOREIGN KEY(fk_wine) REFERENCES wine(pk_wine),
    FOREIGN KEY(fk_user) REFERENCES users(pk_user)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS purchases(
    pk_purchase INTEGER PRIMARY KEY,
    fk_user INTEGER NOT NULL,
    total_value REAL NOT NULL,
    FOREIGN KEY(fk_user) REFERENCES users(pk_user)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS purchase_items(
    pk_item INTEGER PRIMARY KEY,
    fk_purchase INTEGER NOT NULL,
    fk_wine INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY(fk_wine) REFERENCES wines(pk_wine),
    FOREIGN KEY(fk_purchase) REFERENCES purchases(pk_purchase)
)  
''')

for wine in WINES:
    cursor.execute('''
        INSERT INTO wines (brand, name, price, type, alcohol, year, region, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (wine['brand'], wine['name'], wine['price'], wine['type'], wine['alcohol'],
          wine['year'], wine['region'], wine['description']))


for stock in STOCK:
    cursor.execute('''
        INSERT INTO stocks (fk_wine, movement, quantity, fk_user, reason)
        VALUES (?, ?, ?, ?, ?)
    ''', (stock['fk_wine'], stock['movement'], stock['quantity'], stock['fk_user'], stock['reason']))


for purchase in PURCHASES:
    cursor.execute('''
        INSERT INTO purchases (fk_user, total_value)
        VALUES (?, ?)
    ''', (purchase['fk_user'], purchase['total_value']))


for item in PURCHASE_ITEMS:
    cursor.execute('''
        INSERT INTO purchase_items (fk_purchase, fk_wine, quantity)
        VALUES (?, ?, ?)
    ''', (item['fk_purchase'], item['fk_wine'], item['quantity']))

conn.commit()
conn.close()

print("Base de dados inicializada com sucesso!")

