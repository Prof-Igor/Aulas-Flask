from repositories.UserRepository import add_user

def register_new_user(name, email):
    # Lógica de negócios, validações, etc.
    return add_user(name, email)
