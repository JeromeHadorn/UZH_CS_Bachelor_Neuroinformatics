# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie
from moviebox import MovieBox

class Library:

    def __init__(self):
        self.__movies = []

    def add_movie(self, movie):
        self.__movies.append(movie)

    def get_movies(self):
        return self.__recusivelyGettingMovies(self.__movies)

    def __recusivelyGettingMovies(self, movies):
        output = []
        for movie in movies:
            if isinstance(movie, MovieBox):
                output.append(self.__recusivelyGettingMovies(movie.get_movies()))
            else:
                output.append(movie)
        return output

    def get_total_duration(self):
        duration = 0
        for movie in self.__movies:
            duration += movie.get_duration()
        return duration