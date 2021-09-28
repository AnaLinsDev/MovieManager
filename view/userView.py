
from controller.MovieController import MovieController

class UserView():

    def __init__(self):
        self._user_controller = []
        self._movie_controller = MovieController()

    def get_movies(self):
        return self._movie_controller.get_movies()

    def get_favorite_movies(self, user):
        return user.get_favoriteMovies()

    def add_favorite_movies(self, user):
        id = input("Qual id do filme que deseja adicionar ? ")
        for movie in user.get_favoriteMovies():
            if movie.get_key() == int(id):
                return None

        for movie in self._movie_controller.get_movies():
            if movie.get_key() == int(id):
                user.add_favoriteMovies(movie)
                print("Adicionado com Sucesso !")
                return user
            
        return None

    def rem_favorite_movies(self, user):
        id = input("Qual id do filme que deseja adicionar ? ")
        for movie in user.get_favoriteMovies():
            if movie.get_key() == int(id) :
                user.rem_favoriteMovies(movie)
                print("Removido com Sucesso !")
                return user
        return None