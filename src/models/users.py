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

def insert_user(name, dob, email, password, role, vat_number=None, address_1=None, address_2=None):
    password_hash = hash_password(password)
    query = """
        INSERT INTO users (name, dob, email, password_hash, vat_number, address_1, address_2, role)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """
    params = (name, dob, email, password_hash, vat_number, address_1, address_2, role)
    execute_query(query, params)
    logging.info(f"User {name} successfully inserted")

def insert_users(users):
    for user in users:
        password_hash = hash_password(user['password_hash'])
        query = "INSERT INTO users (name, dob, email, password_hash, vat_number, address_1, address_2, role) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
        params = (user['name'], user['dob'], user['email'], password_hash, user['vat_number'], user['address_1'], user['address_2'], user['role'])
        execute_query(query, params)
    logging.info(f"{len(users)} users sucessfully inserted")

def update_user(id, name, dob, email, password, role, vat_number=None, address_1=None, address_2=None):
    password_hash = hash_password(password)
    query = """
        UPDATE users
        SET name = ?, dob = ?, email = ?, password_hash = ?, vat_number = ?, address_1 = ?, address_2 = ?, role = ?
        WHERE pk_user = ?;
    """
    params = (name, dob, email, password_hash, vat_number, address_1, address_2, role, id)
    execute_query(query, params)
    logging.info(f"User {id} successfully updated")

def delete_user(id):
    query = "DELETE FROM users WHERE pk_user = ?;"
    execute_query(query, (id,))
    logging.info(f"User {id} successfully deleted")

def verify_user_credentials(email, password):
    """
    Verifies if the provided email and password match a user in the database.

    :param email: User's email
    :param password: User's password
    :return: True if credentials are correct, False otherwise
    """
    query = "SELECT password_hash FROM users WHERE email = ?;"
    result = fetch_query(query, (email,), fetch_one=True)
    
    if result:
        stored_password_hash = result['password_hash']
        if verify_password(password, stored_password_hash):
            logging.info(f"User {email} successfully authenticated")
            return True
        else:
            logging.warning(f"User {email} failed authentication: incorrect password")
    else:
        logging.warning(f"User {email} failed authentication: email not found")
    
    return False

def get_user_details(email):
    """
    Retrieve user details from the database based on the email.

    :param email: User's email
    :return: Dictionary containing user details (id, email, role)
    """
    query = "SELECT pk_user, email, role FROM users WHERE email = ?;"
    result = fetch_query(query, (email,))

    if result:
        user_details = {
            'id': result[0]['pk_user'],
            'email': result[0]['email'],
            'role': result[0]['role']
        }
        return user_details
    else:
        return None

def get_user_details_by_id(user_id):
    """
    Retrieve user details from the database based on the user ID.

    :param user_id: User's ID
    :return: Dictionary containing user details
    """
    query = "SELECT name, dob, email, password_hash, vat_number, address_1, address_2 FROM users WHERE pk_user = ?;"
    result = fetch_query(query, (user_id,), fetch_one=True)

    if result:
        user_details = {
            'name': result['name'],
            'dob': result['dob'],
            'email': result['email'],
            'password_hash': result['password_hash'],
            'vat_number': result['vat_number'],
            'address_1': result['address_1'],
            'address_2': result['address_2']
        }
        return user_details
    else:
        return None

def update_user_details(user_id, details):
    """
    Update user details in the database.

    :param user_id: User's ID
    :param details: Dictionary containing updated user details
    """
    password_hash = hash_password(details['password_hash'])
    query = """
    UPDATE users
    SET name = ?, dob = ?, email = ?, password_hash = ?, vat_number = ?, address_1 = ?, address_2 = ?
    WHERE pk_user = ?;
    """
    params = (
        details['name'],
        details['dob'],
        details['email'],
        password_hash,
        details['vat_number'],
        details['address_1'],
        details['address_2'],
        user_id
    )
    execute_query(query, params)
    logging.info(f"User {user_id} details successfully updated")
