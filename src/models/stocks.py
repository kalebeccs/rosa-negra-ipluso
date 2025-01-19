import logging
from db.database import execute_query, fetch_query

# "stocks": """
#         CREATE TABLE IF NOT EXISTS stocks(
#             pk_stock INTEGER PRIMARY KEY,
#             fk_wine INTEGER NOT NULL,
#             movement TEXT CHECK(movement IN ('purchase', 'sale', 'adjustment')) NOT NULL,
#             quantity INTEGER NOT NULL,
#             fk_user INTEGER,
#             reason TEXT,
#             FOREIGN KEY(fk_wine) REFERENCES wine(pk_wine),
#             FOREIGN KEY(fk_user) REFERENCES users(pk_user)
#         );
#     """,

def insert_stock(fk_wine, movement, quantity, fk_user, reason):
    query = """
        INSERT INTO stocks (fk_wine, movement, quantity, fk_user, reason)
        VALUES (?, ?, ?, ?, ?);
    """
    params = (fk_wine, movement, quantity, fk_user, reason)
    execute_query(query, params)
    logging.info(f"Stock {fk_wine} sucessfully inserted")

def insert_stocks(stocks):
    for stock in stocks:
        query = "INSERT INTO stocks (fk_wine, movement, quantity, fk_user, reason) VALUES (?, ?, ?, ?, ?);"
        params = (stock['fk_wine'], stock['movement'], stock['quantity'], stock['fk_user'], stock['reason'])
        execute_query(query, params)
    logging.info(f"{len(stocks)} stocks sucessfully inserted")
