from models import User, db

class UserDAO:
    @staticmethod
    def get_user(id):
        return User.query.get(id)

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def add_user(name, email):
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def att_user(id, name, email):
        user = UserDAO.get_user(id)
        if user:
            user.name = name
            user.email = email
            db.session.commit()
        return user

    @staticmethod
    def del_user(id):
        user = UserDAO.get_user(id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user
