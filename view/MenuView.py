from model.User import User
from model.Manager import Manager
from controller.UserController import UserController
from controller.ManagerController import ManagerController

class MenuView():

    def __init__(self):
        self._manager_controller = ManagerController()
        self._user_controller = UserController()

    def login(self):
        print ("\n LOGIN ")
        name = input( 'Nome: ' )
        password = input( 'Senha: ' )
        
        if name.startswith("admin"):
            person = self._manager_controller.login(Manager(name, password))
        else:
            person = self._user_controller.login(User(name, password))

        if person != None :
            print (" Logado ")
        else : 
            print (" Ocorreu um problema ")

        return person  

    def register(self):
        print ("\n REGISTER ")
        name = input( 'Nome: ' )
        password = input( 'Senha: ' )
        
        if name.startswith("admin"):
            person = self._user_controller.register(Manager(name, password))
        else:
            person = self._manager_controller.register(User(name, password))

        if person != None :
            print (" Logado ")
        else : 
            print (" Ocorreu um problema ")

        return person 
        