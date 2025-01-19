import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from db.database import initialize_db
from seed_data import USERS, WINES, STOCK, PURCHASES, PURCHASE_ITEMS
from src.models.users import insert_users
from src.models.wines import insert_wines
from src.models.stocks import insert_stocks
from src.models.purchases import insert_purchases
from src.models.purchases import insert_purchase_items

def seed_data():
    """
    Insert mock data into the database tables.
    """
    try:
        # Insert into tables
        insert_users(USERS)
        insert_wines(WINES)
        insert_stocks(STOCK)
        insert_purchases(PURCHASES)
        insert_purchase_items(PURCHASE_ITEMS)

        logging.info("Mock data inserted successfully!")
    except Exception as e:
        logging.error(f"Error inserting mock data: {e}")
        raise
        
if __name__ == "__main__":
    # Initialize the database
    logging.info("Initializing the database...")
    initialize_db()

    # Populate the database with mock data
    logging.info("Populating the database with mock data...")
    seed_data()
