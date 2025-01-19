import bcrypt

def hash_password(password):
    """
    Hash the password using bcrypt.
    :param password: plain text password
    :return: hashed password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(plain_password, hashed_password):
    """
    Verify if the plain password matches the hashed password.
    :param plain_password: plain text password
    :param hashed_password: hashed password from database
    :return: True if matches, False otherwise
    """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
