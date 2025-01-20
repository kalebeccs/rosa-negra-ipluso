# Global variables to store the user's login state
user_logged_in = False
current_user_id = None
current_user_email = None
current_user_password = None
current_user_role = None

def login_user(user_id, email, password, role):
    global user_logged_in, current_user_id, current_user_email, current_user_password, current_user_role
    user_logged_in = True
    current_user_id = user_id
    current_user_email = email
    current_user_password = password
    current_user_role = role

def logout_user():
    global user_logged_in, current_user_id, current_user_email, current_user_password, current_user_role
    user_logged_in = False
    current_user_id = None
    current_user_email = None
    current_user_password = None
    current_user_role = None

def is_user_logged_in():
    return user_logged_in

def get_current_user_id():
    return current_user_id

def get_current_user_email():
    return current_user_email

def get_current_user_password():
    return current_user_password

def get_current_user_role():
    return current_user_role

def is_user_admin():
    return current_user_role == 'admin'
