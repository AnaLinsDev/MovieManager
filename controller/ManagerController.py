from repository.ManagerRepository import managers

class ManagerController():
    
    def __init__(self):
        self._managers = managers

    def login(self, person):
        for p in self._managers:
            if person.get_name() == p.get_name() and person.get_password() == p.get_password():
                return p
        else :
            print ( "Não Cadastrado" )
            return None

    def register(self, person):

        if person in self._managers:
            print ( "Já foi cadastrado" )
            return None
        else :
            self._managers.append(person)
            return person
        