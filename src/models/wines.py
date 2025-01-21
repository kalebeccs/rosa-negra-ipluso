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

def update_wine(pk_wine, brand, name, price, type, alcohol, year, region, description):
    query = """
        UPDATE wines
        SET brand = ?, name = ?, price = ?, type = ?, alcohol = ?, year = ?, region = ?, description = ?
        WHERE pk_wine = ?;
    """
    params = (brand, name, price, type, alcohol, year, region, description, pk_wine)
    execute_query(query, params)
    logging.info(f"Wine with id {pk_wine} sucessfully updated")

def get_all_wines():
    query = "SELECT * FROM wines;"
    wines = fetch_query(query)
    return wines

def get_wine_by_id(pk_wine):
    query = "SELECT * FROM wines WHERE pk_wine = ?;"
    params = (pk_wine,)
    wine = fetch_query(query, params, fetch_one=True)
    return wine

def get_wines_by_type(wine_type):
    query = "SELECT * FROM wines WHERE type = ?;"
    params = (wine_type,)
    wines = fetch_query(query, params)
    return wines

def delete_wine(pk_wine):
    query = "DELETE FROM wines WHERE pk_wine = ?;"
    params = (pk_wine,)
    execute_query(query, params)
    logging.info(f"Wine with id {pk_wine} sucessfully deleted")
