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



def add_purchase_item(purchase_id, wine_id, quantity):
    """
    Add an item to a purchase in the database.

    :param purchase_id: ID of the purchase
    :param wine_id: ID of the wine being purchased
    :param quantity: Quantity of the wine being purchased
    """
    query = "INSERT INTO purchase_items (fk_purchase, fk_wine, quantity) VALUES (?, ?, ?);"
    params = (purchase_id, wine_id, quantity)
    execute_query(query, params)
    logging.info(f"Purchase item {purchase_id} successfully added")

def get_purchase_details(purchase_id):
    """
    Retrieve details of a purchase from the database.

    :param purchase_id: ID of the purchase
    :return: Dictionary containing purchase details and items
    """
    purchase_query = "SELECT pk_purchase, fk_user, total_value FROM purchases WHERE pk_purchase = ?;"
    items_query = "SELECT fk_wine, quantity FROM purchase_items WHERE fk_purchase = ?;"
    
    purchase = fetch_query(purchase_query, (purchase_id,), fetch_one=True)
    items = fetch_query(items_query, (purchase_id,))
    
    if purchase:
        purchase_details = {
            'purchase_id': purchase['pk_purchase'],
            'user_id': purchase['fk_user'],
            'total_value': purchase['total_value'],
            'items': [{'wine_id': item['fk_wine'], 'quantity': item['quantity']} for item in items]
        }
        return purchase_details
    else:
        return None

def get_all_purchases():
    """
    Retrieve all purchases from the database.

    :return: List of dictionaries containing purchase details
    """
    query = "SELECT pk_purchase, fk_user, total_value FROM purchases;"
    purchases = fetch_query(query)

    purchase_list = []
    for purchase in purchases:
        purchase_details = get_purchase_details(purchase['pk_purchase'])
        if purchase_details:
            purchase_list.append(purchase_details)
    
    return purchase_list

def get_sales_data():
    """
    Retrieve sales data from the database.
    :return: List of dictionaries containing sales data
    """
    query = """
    SELECT 
        wines.type AS wine_type,
        wines.name AS wine_name,
        purchase_items.quantity AS quantity_sale,
        (purchase_items.quantity * wines.price) AS total_value
    FROM 
        purchase_items
    JOIN 
        wines ON purchase_items.fk_wine = wines.pk_wine;
    """
    return fetch_query(query)
