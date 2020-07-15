# The signatures of this class and its public methods are required for the automated
# grading to work. You must not change the names or the list of parameters. You may
# introduce private/protected utility methods though.
class Fridge:

    def __init__(self):
        self.__items = []

    def store(self, item):
        self.__items.append(item)


    def take(self, item):
        if item in self.__items:
            index = self.__items.index(item)
            self.__items.pop(index)
            return item
        else:
            raise Warning("not in the fridge")


    def find(self, name):
        for item in sorted(self.__items, key=lambda x: x[0], reverse=False):
            if item[1] == name:
                return item
            else:
                return None

    def take_before(self, date):
        tobeRemoved = []
        for item in sorted(self.__items, key=lambda x: x[0], reverse=False):
            if item[0] < date:
                tobeRemoved.append(item)

        if len(tobeRemoved) == 0:
            return []
        else:
            for item in tobeRemoved:
                index = self.__items.index(item)
                self.__items.pop(index)
            return tobeRemoved

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        return iter(sorted(self.__items, key=lambda x: x[0], reverse=False))

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    l = ["a", "b", "c"]
    for i in l:
        l.remove(i)

    f = Fridge()
    f.store((191127, "Butter"))
    f.store((191117, "Milk"))

    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))

    i = f.take((191127, "Butter"))
    print("Removed {}, {} items left".format(i, len(f)))

    # j = f.take((191117, "Milk"))
    # print("Removed {}, {} items left".format(j, len(f)))

    print("found:",f.find("Milk1"))

    print(f.take_before(191118))

    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))