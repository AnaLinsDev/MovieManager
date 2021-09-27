from Person import Person

class   Manager(Person):
    
    def get_name(self):
        return self._name
    def set_name(self, new):
         self._name = new

    def get_password(self):
        return self._password
    def set_password(self, new):
        self._password = new

    def set_id(self, new):
         self._id = new
    def get_id(self):
        return self._id
        