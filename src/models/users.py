import logging
from db.database import execute_query, fetch_query
from src.utils import hash_password, verify_password

# "users": """
#         CREATE TABLE IF NOT EXISTS users (
#             pk_user INTEGER PRIMARY KEY,
#             name TEXT NOT NULL,
#             dob DATE NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             password_hash TEXT NOT NULL,
#             vat_number INTEGER,
#             address_1 TEXT,
#             address_2 TEXT,
#             role TEXT NOT NULL
#         );
#     """,

def insert_user(name, dob, email, password, vat_number, address_1, address_2, role):
    password_hash = hash_password(password)
    query = """
        INSERT INTO users (name, dob, email, password_hash, vat_number, address_1, address_2, role)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """
    params = (name, dob, email, password_hash, vat_number, address_1, address_2, role)
    execute_query(query, params)
    logging.info(f"User {name} sucessfully inserted")

def insert_users(users):
    for user in users:
        password_hash = hash_password(user['password_hash'])
        query = "INSERT INTO users (name, dob, email, password_hash, vat_number, address_1, address_2, role) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
        params = (user['name'], user['dob'], user['email'], password_hash, user['vat_number'], user['address_1'], user['address_2'], user['role'])
        execute_query(query, params)
    logging.info(f"{len(users)} users sucessfully inserted")
