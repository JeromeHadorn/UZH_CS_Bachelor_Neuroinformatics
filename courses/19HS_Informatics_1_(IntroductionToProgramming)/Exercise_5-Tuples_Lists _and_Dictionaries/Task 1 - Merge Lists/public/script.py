# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
def merge(a, b):
    a_length = len(a)
    b_length = len(b)

    if a_length == 0:
        return []
    elif b_length == 0:
        return []
    else:
        list_of_tuples = []

        shortList = []
        longerList = []
        if a_length > b_length:
            shortList = b
            longerList = a
        else:
            shortList = a
            longerList = b

        lastShort = shortList[0]
        lastLong = longerList[0]

        for index, item in enumerate(longerList):
            if index < len(shortList):
                lastShort = shortList[index]
            lastLong = longerList[index]

            if a_length > b_length:
                list_of_tuples.append((lastLong,lastShort))
            else:
                list_of_tuples.append((lastShort, lastLong))
        return list_of_tuples

    


# You can play around with your solution from within this block.
if __name__ == '__main__':
    print(merge([0, 1, 2], [5, 6]))

#Write a function that expects two lists of integers, a and b, as parameters. The function should merge the elements of both lists by index and store them as tuples in a new list. If one list is shorter than the other, the last element of the shorter list should be repeated as often as necessary. If one of both lists is empty, the result should be the empty list.

#Please consider the following example:

#merge([0, 1, 2], [5, 6]) -> [(0, 5), (1, 6), (2, 6)]

#You can assume that the parameters are always valid lists and you do not need to provide any kind of input validation.

#Note: The provided script defines the signature of the function. Do not change this signature or the automated grading will fail.