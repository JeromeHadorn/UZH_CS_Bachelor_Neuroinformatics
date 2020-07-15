# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie

class MovieBox(Movie):

    def __init__(self, title, movies):
        self.__title = title
        self.__movies = movies

        for movie in self.__movies:
            if not isinstance(movie, Movie):
                raise Warning


    def __repr__(self):

        movies = []
        for movie in self.__movies:
            movies.append(movie)


        return "MovieBox(\"{}\", {})".format(self.__title, movies)

    def __eq__(self, other):
        if self.__hash__() == other.__hash__():
            return True
        else:
            return False

    def __hash__(self):
        hash = 0
        for movie in self.__movies:
            hash += movie.__hash__()
        return hash

    def get_title(self):
        return self.__title

    def get_movies(self):
        return self.__movies[:]

    def get_actors(self):
        actors = []
        for movie in self.__movies:
            for actor in movie.get_actors():
                if actor not in actors:
                    actors.append(actor)

        actors = sorted(actors)
        return actors[:]

    def get_duration(self):
        duration = 0
        for movie in self.__movies:
            duration += movie.get_duration()
        return duration

    # also implement the required special functions
