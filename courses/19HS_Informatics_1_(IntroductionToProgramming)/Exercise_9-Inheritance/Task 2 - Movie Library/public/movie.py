# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:

    def __init__(self, title, actors, duration):
        self.__title = title
        self.__actors = sorted(actors)
        self.__duration = duration

        if title == "":
            raise Warning
        if actors == []:
            raise Warning
        if not isinstance(duration,int) or duration < 1:
            raise Warning

    def __repr__(self):
        string = 'Movie("{}", {}, {})'.format(self.__title, repr(self.get_actors()), self.__duration)
        string = string.replace("\'", "\"")
        return string

    def __eq__(self, other):
        if self.__hash__() == other.__hash__():
            return True
        else:
            return False

    def __hash__(self):

       return int(self.__title.encode('ascii') + "".join(self.__actors).encode('ascii') * self.__duration)

    def get_title(self):
        return self.__title

    def get_actors(self):
        return self.__actors[:]

    def get_duration(self):
        return self.__duration

    # also implement the required special functions
