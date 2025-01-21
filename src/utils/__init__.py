import re
import bcrypt
from datetime import datetime, timedelta

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

def validate_dob(dob):
    """
    Validate the date of birth format (YYYY-MM-DD).
    :param dob: date of birth string
    :return: True if valid, False otherwise
    """
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    return re.match(pattern, dob) is not None

def validate_email(email):
    """
    Validate the email format.
    :param email: email address string
    :return: True if valid, False otherwise
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def is_of_age(dob, age_limit=18):
    """
    Check if the age is greater than or equal to the specified age limit.
    :param dob: date of birth string (YYYY-MM-DD)
    :param age_limit: age limit to check against (default is 18)
    :return: True if age is greater than or equal to age_limit, False otherwise
    """
    dob_date = datetime.strptime(dob, "%Y-%m-%d")
    age = (datetime.now() - dob_date) // timedelta(days=365.2425)
    return age >= age_limit

def validate_required_fields(*fields):
    """
    Validate that all required fields are filled.
    :param fields: list of fields to check
    :return: True if all fields are filled, False otherwise
    """
    return all(fields)

def validate_vat_number(vat_number):
    """
    Validate the Portuguese VAT number (NIF).
    :param vat_number: VAT number string
    :return: True if valid, False otherwise
    """
    if not vat_number.isdigit() or len(vat_number) != 9:
        return False

    check_digit = int(vat_number[-1])
    total = sum(int(digit) * (9 - idx) for idx, digit in enumerate(vat_number[:-1]))
    calculated_check_digit = 11 - (total % 11)
    if calculated_check_digit >= 10:
        calculated_check_digit = 0

    return check_digit == calculated_check_digit
