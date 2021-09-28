from model.Movie import Movie
from repository.MovieRepository import movies

class MovieController():
    
    def __init__(self):
        self._movies = movies

    def get_movies(self):
        return self._movies
    
    def add_movies(self, name, year):
        id = 0
        for m in self._movies:
            if m.get_key() > id:
                id = m.get_key()

        movie = Movie(name, year, id + 1)
        self._movies.append(movie)
        return self._movies

    def rem_movies(self, id):
        try:
            self._movies.pop(int(id))
            return self._movies
        except:
            return None
        

    def update_movie(self, id, name, year):
        try:
            self._movies[int(id)].set_name(name)
            self._movies[int(id)].set_year(year)
            return self._movies
        except:
            return None