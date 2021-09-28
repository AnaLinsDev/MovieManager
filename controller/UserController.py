from model.Movie import Movie

class MovieController():
    
    def __init__(self):
        self._movies = [Movie("Avengers", "2012"), Movie("Moana", "2016")]

    def get_movies(self):
        return self._movies
