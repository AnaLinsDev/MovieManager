from model.Manager import Manager
from model.User import User
from controller.MovieController import MovieController
from controller.UserController import UserController

class UserView():

    def __init__(self):
        self._user_controller = UserController()
        self._movie_controller = MovieController()

    def login(self):
        print ("\n LOGIN ")
        name = input( 'Nome: ' )
        password = input( 'Senha: ' )
        
        if name.startswith("admin"):
            person = self._user_controller.login(User(name, password))
        else:
            person = self._user_controller.login(Manager(name, password))

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
            person = self._user_controller.register(User(name, password))

        if person != None :
            print (" Logado ")
        else : 
            print (" Ocorreu um problema ")

        return person 
        
    def get_movies(self):
        movies =  self._movie_controller.get_movies()
        for m in movies :
            print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")

    def get_favorite_movies(self, user):
        movies  = user.get_favoriteMovies()
        for m in movies :
            print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")


    def add_favorite_movies(self, user):

        print ("\nFILMES: ")
        movies = self._movie_controller.get_movies()
        for m in movies :
            print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")

        id = input("Qual id do filme que deseja adicionar ? ")
        for movie in user.get_favoriteMovies():
            if movie.get_key() == int(id):
                print("Ocorreu um problema : Filme já adicionado\n")
                return None

        for movie in self._movie_controller.get_movies():
            if movie.get_key() == int(id):
                user.add_favoriteMovies(movie)
                print("Adicionado com Sucesso !\n")
                return user

        print("Ocorreu um problema\n")
        return None

    def rem_favorite_movies(self, user):

        movies  = user.get_favoriteMovies()
        for m in movies :
            print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")

        id = input("Qual id do filme que deseja remover ? ")
        for movie in user.get_favoriteMovies():
            if movie.get_key() == int(id) :
                user.rem_favoriteMovies(movie)
                print("Removido com Sucesso !\n")
                return user

        print("Ocorreu um problema\n")
        return None