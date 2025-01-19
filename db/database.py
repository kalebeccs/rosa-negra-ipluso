import sqlite3
import logging
from db.db_schemas import TABLES

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DatabaseManager:
    """
    Manages the database connection using Python's context management.

    Methods:
        __enter__: Opens the database connection.
        __exit__: Closes the connection when exiting the context.
    """
    def __init__(self, db_path='db/rosa_negra.db'):
        self.db_path = db_path

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
            return self.conn
        except sqlite3.Error as e:
            logging.error(f"Error connecting to the database: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

def execute_query(query, params=None, trim=False):
    """
    Executes a query on the database.
    :param query: string with the query to be executed.
    :param params: tuple with the query parameters.
    :return: cursor with the query results.
    """
    with DatabaseManager() as conn:
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            logging.info(f"Query executed: {query}")
            return cursor
        except sqlite3.Error as e:
            logging.error(f"Error executing query: {e}")
            raise

def fetch_query(query, params=None, fetch_one=False):
    """
    Executes a query on the database and returns the results.
    :param query: string with the query to be executed.
    :param params: tuple with the query parameters.
    :param fetch_one: boolean to return only one result.
    :return: list with the query results.
    """
    with DatabaseManager() as conn:
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchone() if fetch_one else cursor.fetchall()
            if fetch_one and results:
                return dict(results)
            elif results:
                return [dict(row) for row in results] 
            else:
                return None
        except sqlite3.Error as e:
            logging.error(f"Error fetching data: {e}")
            return None

def fetch_all_from_table(table_name):
    """
    Returns all records from a specific table.
    :param table_name: Name of the table.
    :return: List of dictionaries containing the table records.
    """
    if table_name not in TABLES.keys():
        raise ValueError(f"Table '{table_name}' not allowed. Valid tables: {', '.join(TABLES.keys())}")
    return fetch_query(f"SELECT * FROM {table_name}")

def initialize_db():
    """
    Initializes the database, creating the necessary tables if they do not exist.
    """
    with DatabaseManager() as conn:
        try:
            cursor = conn.cursor()
            conn.execute("BEGIN")
            for table_name, create_statement in TABLES.items():
                cursor.execute(create_statement)
                logging.info(f"Table '{table_name}' verified/created successfully.")
            conn.commit()
            logging.info("Database initialized successfully!")
        except sqlite3.Error as e:
            conn.rollback()
            logging.error(f"Error initializing database: {e}")
            raise
