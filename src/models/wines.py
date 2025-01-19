import logging
from db.database import execute_query, fetch_query

# "wines": """
#         CREATE TABLE IF NOT EXISTS wines(
#             pk_wine INTEGER PRIMARY KEY,
#             brand TEXT NOT NULL, 
#             name TEXT NOT NULL,
#             price REAL NOT NULL,
#             type TEXT NOT NULL,
#             alcohol REAL NOT NULL,
#             year INTEGER NOT NULL,
#             region TEXT NOT NULL,
#             description TEXT NOT NULL
#         );
#     """,

def insert_wine(brand, name, price, type, alcohol, year, region, description):
    query = """
        INSERT INTO wines (brand, name, price, type, alcohol, year, region, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """
    params = (brand, name, price, type, alcohol, year, region, description)
    execute_query(query, params)
    logging.info(f"Wine {name} sucessfully inserted")

def insert_wines(wines):
    for wine in wines:
        query = "INSERT INTO wines (brand, name, price, type, alcohol, year, region, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
        params = (wine['brand'], wine['name'], wine['price'], wine['type'], wine['alcohol'], wine['year'], wine['region'], wine['description'])
        execute_query(query, params)
    logging.info(f"{len(wines)} wines sucessfully inserted")
