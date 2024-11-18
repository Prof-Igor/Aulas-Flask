from models.User import User, db

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def add_user(name, email):
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return user

def att_user(id, name, email):
    user = get_user(id)
    user.name = name
    user.email = email
    db.session.commit()
    return user

def del_user(id):
    user = get_user(id)
    db.session.delete(user)
    db.session.commit()
    return user
