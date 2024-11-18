from dao import UserDAO

class UserRepository:
    def __init__(self) -> None:
        self.userDao = UserDAO()

    def get_all_users(self):
        return self.userDao.get_all_users()

    def get_user_by_id(self, user_id):
        return self.userDao.get_user_by_id(user_id)

    def create_user(self, name, email):
        return self.userDao.create_user(name, email)

    def update_user(self, user_id, name, email):
        return self.userDao.update_user(user_id, name, email)

    def delete_user(self, user_id):
        return self.userDao.delete_user(user_id)
