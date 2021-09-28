from controller.MovieController import MovieController

class ManagerView():

    def __init__(self):
        self._movie_controller = MovieController()

    def get_movies(self):
        movies = self._movie_controller.get_movies()
        print ("\nFILMES: ")
        for m in movies :
            print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")

    def add_movies(self):
        name = input("Nome do filme: ")
        year = input("Ano do filme: ")
        movies = self._movie_controller.add_movies(name, year)

        print ("\nNova lista de filme")
        if movies != None:
            for m in movies :
                print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")

    def rem_movies(self):
        movies = self._movie_controller.get_movies()
        print ("\nLista de filmes")
        if movies != None:
            for m in movies :
                print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")

        id = input("Qual id deseja remover ?: ")

        newMovies = self._movie_controller.rem_movies(id)
        print ("\nNova lista de filme")
        if newMovies != None:
            for m in newMovies :
                print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        else :
            print ("Ocorreu um problema")
        print ("\n")


    def update_movies(self):

        movies = self._movie_controller.get_movies()
        print ("\nLista de filmes")
        if movies != None:
            for m in movies :
                print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")


        id   = input("id para atualizar filme :: ")
        name = input("Novo nome do filme: ")
        year = input("Novo ano do filme: ")


        movies = self._movie_controller.update_movie(id, name, year)

        print ("\nNova lista de filme")
        if movies != None:
            for m in movies :
                print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")