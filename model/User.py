from model.Person import Person
from model.Movie import Movie

class User(Person):
    
    def __init__(self, name=None, password=None):
        self._name = name
        self._password = password
        self._favoriteMovies = [Movie("Avengers", "2012", 0)]

    def get_name(self):
        return self._name
    def set_name(self, new):
         self._name = new

    def get_password(self):
        return self._password
    def set_password(self, new):
        self._password = new

    def get_favoriteMovies(self):
        return self._favoriteMovies
    def add_favoriteMovies(self, movie):
        self._favoriteMovies.append( movie )
    def rem_favoriteMovies(self, movie):
        self._favoriteMovies.remove( movie )

