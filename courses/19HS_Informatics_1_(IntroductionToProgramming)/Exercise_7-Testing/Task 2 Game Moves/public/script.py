# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def move(state, direction):
    state_check_sensibleSize(state)
    state_check_characters(state)
    state_check_linelength(state)
    state_check_onlyOnePlayer(state)
    state_check_oneMoveAtleastPossible(state, direction)
    move_check_providedMoveisPossible(state, direction)

    newState = return_newState(state, direction)
    newPossibleMoves = return_newPossibleMoves(newState)
    print("at the end")
    return (newState,newPossibleMoves)

def return_newPossibleMoves(state):
    directions = []
    (playerRow, playerColumn) = helper_getPlayerLocation(state)

    up = is_upPossible((playerRow,playerColumn),state)
    down = is_downPossible((playerRow, playerColumn), state)
    left = is_leftPossible((playerRow, playerColumn), state)
    right = is_rightPossible((playerRow, playerColumn), state)

    if down == True:
        directions.append("down")
    if left == True:
        directions.append("left")
    if right == True:
        directions.append("right")
    if up == True:
        directions.append("up")

    return tuple(directions)


def return_newState(oldState,direction):
    state = list(oldState)
    (playerRow, playerColumn) = helper_getPlayerLocation(state)

    if direction == "down":
        down = is_downPossible((playerRow, playerColumn), state)
        if down == True:
            #state[playerRow][playerColumn] = " "
            #state[playerRow+1][playerColumn] = "o"

            text = state[playerRow]
            new = list(text)
            new[playerColumn] = ' '
            state[playerRow] = ''.join(new)

            text = state[playerRow+1]
            new = list(text)
            new[playerColumn] = 'o'
            state[playerRow+1] = ''.join(new)


            return tuple(state)
    elif direction == "left":
        left = is_leftPossible((playerRow, playerColumn), state)
        if left == True:
           # state[playerRow][playerColumn] = " "
            #state[playerRow][playerColumn-1] = "o"

            text = state[playerRow]
            new = list(text)
            new[playerColumn] = ' '
            state[playerRow] = ''.join(new)

            text = state[playerRow]
            new = list(text)
            new[playerColumn -1] = 'o'
            state[playerRow] = ''.join(new)

            return tuple(state)
    elif direction == "right":
        right = is_rightPossible((playerRow, playerColumn), state)
        if right == True:
            # state[playerRow][playerColumn] = " "
            # state[playerRow][playerColumn+1] = "o"

            text = state[playerRow]
            new = list(text)
            new[playerColumn] = ' '
            state[playerRow] = ''.join(new)

            text = state[playerRow]
            new = list(text)
            new[playerColumn + 1] = 'o'
            state[playerRow] = ''.join(new)
            return tuple(state)
    elif direction == "up":
        up = is_upPossible((playerRow, playerColumn), state)
        if up == True:
            # state[playerRow][playerColumn] = " "
            # state[playerRow-1][playerColumn] = "o"

            text = state[playerRow]
            new = list(text)
            new[playerColumn] = ' '
            state[playerRow] = ''.join(new)

            text = state[playerRow-1]
            new = list(text)
            new[playerColumn] = 'o'
            state[playerRow-1] = ''.join(new)
            return tuple(state)

def state_check_sensibleSize(state):
    zeroRow = False

    for row in state:
        if len(row) == 0:
            zeroRow = True

    if len(state) == 0 or zeroRow == True:
        raise Warning("not sensible Size")

def state_check_characters(state):
    badCharacters = False
    allowedCharacters = [" ", "#", "o"]
    for row in state:
        for character in row:
            if not character in allowedCharacters:
                badCharacters = True
    if badCharacters == True:
        raise Warning("bad characters")

def state_check_linelength(state):
    lengths = []
    for line in state:
        lengths.append(len(line))

    if len(lengths) == 0:
        raise Warning("not sensible size 2")

    sizeToMatch = lengths[0]
    for length in lengths:
        if length != sizeToMatch:
            raise Warning("all lines aren't same length")


def state_check_onlyOnePlayer(state):
    playerCounter = 0
    for row in state:
        for character in row:
            if character == "o":
                playerCounter += 1

    if playerCounter != 1:
        raise  Warning("not just one player in map")


def state_check_oneMoveAtleastPossible(state, direction):
    (playerRow, playerColumn) = helper_getPlayerLocation(state)

    up = is_upPossible((playerRow,playerColumn),state)
    down = is_downPossible((playerRow, playerColumn), state)
    left = is_leftPossible((playerRow, playerColumn), state)
    right = is_rightPossible((playerRow, playerColumn), state)
    directionPossibilities = [up,down,left,right]
    if not True in directionPossibilities:
        raise Warning("no direction is possible")






def move_check_providedMoveisPossible(state, direction):
    (playerRow, playerColumn) = helper_getPlayerLocation(state)

    if direction == "down":
        down = is_downPossible((playerRow, playerColumn), state)
        if down == False:
            raise Warning("given direction down not possible")
    elif direction == "left":
        left = is_leftPossible((playerRow, playerColumn), state)
        if left == False:
            raise Warning("given direction left not possible")
    elif direction == "right":
        right = is_rightPossible((playerRow, playerColumn), state)
        if right == False:
            raise Warning("given direction right not possible")
    elif direction == "up":
        up = is_upPossible((playerRow, playerColumn), state)
        if up == False:
            raise Warning("given direction up not possible")
    else:
        raise Warning("no direction given")

def is_leftPossible(location,state):
    if location[1] == 0:
        return False
    elif state[location[0]][location[1] -1] == " ":
        return True
    else:
        return False

def is_rightPossible(location,state):
    if location[1] == len(state[location[0]]) -1:
        return False
    elif state[location[0]][location[1] +1] == " ":
        return True
    else:
        return False

def is_upPossible(location,state):
    if  location[0] == 0:
        return False
    elif state[location[0]-1][location[1]] == " ":
        return True
    else:
        return False
def is_downPossible(location,state):
    if location[0] == len(state) - 1:
        return False
    elif state[location[0]+1][location[1]] == " ":
        return True
    else:
        return False


def helper_getPlayerLocation(state):
    for rowindex, row in enumerate(state):
        for columnindex, column in enumerate(row):
            if column == "o":
                return (rowindex, columnindex)


if __name__ == "__main__":
    s1 = (
        "#####   ",
        "###    #",
        "#   o ##",
        "   #####"
    )
    s2 = move(s1, "right")

    print("= New State =")
    print("\n".join(s2[0]))
    print("\nPossible Moves: {}".format(s2[1]))
