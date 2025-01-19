import logging
from db.database import execute_query, fetch_query

# "purchases": """
#         CREATE TABLE IF NOT EXISTS purchases(
#             pk_purchase INTEGER PRIMARY KEY,
#             fk_user INTEGER NOT NULL,
#             total_value REAL NOT NULL,
#             FOREIGN KEY(fk_user) REFERENCES users(pk_user)
#         );
#     """,
#     "purchase_items": """
#         CREATE TABLE IF NOT EXISTS purchase_items(
#             pk_item INTEGER PRIMARY KEY,
#             fk_purchase INTEGER NOT NULL,
#             fk_wine INTEGER NOT NULL,
#             quantity INTEGER NOT NULL,
#             FOREIGN KEY(fk_wine) REFERENCES wines(pk_wine),
#             FOREIGN KEY(fk_purchase) REFERENCES purchases(pk_purchase)
#         );
#     """

def insert_purchase(fk_user, total_value):
    query = """
        INSERT INTO purchases (fk_user, total_value)
        VALUES (?, ?);
    """
    params = (fk_user, total_value)
    execute_query(query, params)
    logging.info(f"Purchase {fk_user} sucessfully inserted")

def insert_purchase_item(fk_purchase, fk_wine, quantity):
    query = """
        INSERT INTO purchase_items (fk_purchase, fk_wine, quantity)
        VALUES (?, ?, ?);
    """
    params = (fk_purchase, fk_wine, quantity)
    execute_query(query, params)
    logging.info(f"Purchase item {fk_purchase} sucessfully inserted")

def insert_purchases(purchases):
    for purchase in purchases:
        query = "INSERT INTO purchases (fk_user, total_value) VALUES (?, ?);"
        params = (purchase['fk_user'], purchase['total_value'])
        execute_query(query, params)
    logging.info(f"{len(purchases)} purchases sucessfully inserted")

def insert_purchase_items(purchase_items):
    for purchase_item in purchase_items:
        query = "INSERT INTO purchase_items (fk_purchase, fk_wine, quantity) VALUES (?, ?, ?);"
        params = (purchase_item['fk_purchase'], purchase_item['fk_wine'], purchase_item['quantity'])
        execute_query(query, params)
    logging.info(f"{len(purchase_items)} purchase items sucessfully inserted")
