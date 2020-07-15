def compress(data):
    dictionaryForLetter = {}
    arrayToStore = []
    arrayOfTuples = []

    for row in data:
        for key in row.keys():
            if key in dictionaryForLetter:
                previousValues = dictionaryForLetter[key]
                previousValues.append(row[key])
                dictionaryForLetter[key] = previousValues
            else:
                dictionaryForLetter[key] = [row[key]]

    keys = []
    for key in dictionaryForLetter:
        keys.append(key)


    keys.sort()

    for index, key in enumerate(keys):
        print(index)
        if index == 0:
            for secIndex, number in enumerate(dictionaryForLetter[key]):
                arrayToStore.append([number])
        else:
            for secIndex, number in enumerate(dictionaryForLetter[key]):
                print(secIndex,arrayToStore)
                oldValue = arrayToStore[secIndex]
                print(oldValue,"oldvalue")
                oldValue.append(number)
                newValue = oldValue
                print(newValue, "newValue")
                arrayToStore[secIndex] = newValue




    #print(arrayToStore)

    for alist in arrayToStore:
        arrayOfTuples.append(tuple(alist))

    counter = 0
    for row in data:
        if row == {}:
            counter = counter + 1
            print("is empty")
            print(len(data),counter)
    if counter == len(data):
        print("hit")
        for row in data:
            arrayOfTuples.append(tuple())



    return (tuple(keys),arrayOfTuples)