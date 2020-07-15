# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
def invert(d):
    copy = d.copy()
    invertedD = {}
    for key in copy.keys():
        value = copy[key]
        if value in invertedD:
            previousValue = invertedD[value]
            previousValue.append(key)
            previousValue.sort()
            invertedD[value] = previousValue
        else:
            invertedD[value] = [key]
    return invertedD


# You can play around with your solution from within this block.
if __name__ == '__main__':
    print(invert({"a":1, "b":1, "c":3}))
