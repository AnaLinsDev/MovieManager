from controller.UserController import UserController

class MainController():
    
    def __init__(self):
        self._users = UserController().get_users()

    def get_users(self):
        return self._users

    def login(self, person):
        for p in self._users:
            if person.get_name() == p.get_name() and person.get_password() == p.get_password():
                return p
        else :
            print ( "Não Cadastrado" )
            return None

    def register(self, person):

        for p in self._users:
            print(p.get_name())

        if person in self._users:
            print ( "Já foi cadastrado" )
            return None
        else :
            self._users.append(person)
            return person
        