
from model.User import User
from model.Manager import Manager
from controller.MainController import MainController

class MainView():

    def __init__(self):

        self._main_controller = MainController()

    def login(self):
        print ("\n LOGIN ")
        name = input( 'Nome: ' )
        password = input( 'Senha: ' )
        
        if name.startswith("admin"):
            return self._main_controller.login(User(name, password))
        else:
            return self._main_controller.login(Manager(name, password))

    def register(self):
        print ("\n REGISTER ")
        name = input( 'Nome: ' )
        password = input( 'Senha: ' )
        
        if name.startswith("admin"):
            return self._main_controller.register(User(name, password))
        else:
            return self._main_controller.register(Manager(name, password))