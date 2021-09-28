from model.Person import Person

class MainController():
    
    def __init__(self):
        self._users = []


    def login(self, person):
        if person in self._users:
            return True
        else :
            return False


    def cadastro(self, newPerson):
        if newPerson in self._users:
            return False
        else :
            self._users.append(newPerson)
            return True
        