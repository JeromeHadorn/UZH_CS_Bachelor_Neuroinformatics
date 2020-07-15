# The signatures of this class and its public methods are required for the automated
# grading to work. You must not change the names or the list of parameters. You may
# introduce private/protected utility methods though.
class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__title = title
        self.__year = year

    def get_authors(self):
        return self.__authors[:]

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def __str__(self):
        stra = str(self.__authors)
        title = str(self.get_title())
        return "Publication(" + stra.replace("'", '"') + ", " + '"' + title + '"' + ", " + str(self.get_year()) + ")"
    def __repr__(self):
        stra = str(self.__authors)
        title = str(self.get_title())
        return "Publication(" + stra.replace("'", '"') + ", " + '"' + title + '"' + ", " + str(self.get_year()) + ")"

    def __eq__(self, y):
        if isinstance(y, Publication):
            if self.__hash__() == y.__hash__():
                #print("the fuckin same", self.__hash__() , y.__hash__())
                return True
            else:
                return False
        else:
            return NotImplemented

    def __hash__(self):
        return hash(("".join(self.__authors), self.__title, self.__year))


    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        else:
            if self.__authors == other.__authors:
                return self.__year < other.__year
            else:
                return self.__authors < other.__authors

    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        else:
            if self.__authors == other.__authors:
                return self.__year < other.__year
            else:
                return self.__authors <= other.__authors


    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        else:
            if self.__authors == other.__authors:
                return self.__year > other.__year
            else:
                return self.__authors > other.__authors

    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        else:
            return self.__authors >= other.__authors

    def __ne__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        else:
            return (self.__hash__() != other.__hash__())

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    assert str(p) == s

    p1 = Publication(["A","B"], "B", 1235)
    p2 = Publication(["A","B"], "B", 1235)
    p3 = Publication(["B"], "C", 2345)


    print(p1 <= p2)

    sales = {
        p1: 273,
        p2: 398,
    }
