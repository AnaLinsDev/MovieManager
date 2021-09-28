from model.Movie import Movie
from model.User import User


class UserController():
    
    def __init__(self):
        self._users = [User("ana", "123", 0)]

    def get_users(self):
        return self._users
    
    def update_user_by_id(self, id):
        for u in self.get_users():
            if u.get_key() == id :
                # QUANDO ESTIVER USANDO BANCO
                return
