class Movie:
    def __init__(self, name=None, year=None, key=None):
        self._name = name
        self._year = year
        self._key = key

    def get_name(self):
        return self._name
    def set_name(self, new):
         self._name = new

    def get_year(self):
        return self._year
    def set_year(self, new):
        self._year = new

    def get_key(self):
        return self._key
