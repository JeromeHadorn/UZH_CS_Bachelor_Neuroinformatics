# The signatures of this class and its public methods are required for the automated
# grading to work. You must not change the names or the list of parameters. You may
# introduce private/protected utility methods though.
class MagicDrawingBoard:
    def __init__(self, x, y):
        self.__xSize = x
        self.__ySize = y
        if x < 1 or y < 1:
            raise Warning
        self.__values = []

    def __isInBoard(self,coordinate):
        values = []
        for i in range(0,self.__ySize):
            for j in range(0,self.__xSize):
                values.append[(i,j)]

        if coordinate not in values:
            raise Warning

    def __checkSize(self,coordinate,coordinate2):
        print(coordinate2[0] <= coordinate[0])
        if coordinate2[0] <= coordinate[0] or coordinate2[1] <= coordinate[1]:
            raise Warning


    def reset(self):
        self.__values = []

    def pixel(self, xy):
        self.__isInBoard(xy)
        self.__values.append(xy)

    def rect(self, start_xy, end_xy):
        self.__checkSize(start_xy,end_xy)
        for i in range(start_xy[0],end_xy[0]):
            for j in range(start_xy[1],end_xy[1]):
                #print(i,j)
                self.__values.append((i,j))

        print(self.__values)

    def img(self):
        lines = []
        for i in range(0,self.__ySize):
            for j in range(0,self.__xSize):
                #print(i, j)
                if (j,i) in self.__values:
                    lines.append("1")
                else:
                    lines.append("0")
            if i != self.__ySize-1:
                lines.append("\n")

        return "".join(lines)

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(6, 4)
    #db.pixel((1, 1))
    db.rect((0, 0), (0, 0))
    db.rect((2, 2), (5, 4))
    print("After drawing:")
    print(db.img())
    db.reset()
    print("After resetting:")
    print(db.img())
