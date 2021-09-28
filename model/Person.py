class Person():
    def __init__(self, name=None, password=None):
        self._name = name
        self._password = password

    def get_name(self):
        return self._name
    def set_name(self, new):
         self._name = new

    def get_password(self):
        return self._password
    def set_password(self, new):
        self._password = new
