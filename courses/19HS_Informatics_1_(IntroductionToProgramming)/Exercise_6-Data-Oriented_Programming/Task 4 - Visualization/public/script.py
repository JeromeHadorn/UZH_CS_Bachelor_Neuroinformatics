# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
def visualize(records):
    survived_index = -1
    Pclass_index = -1
    name_index = -1
    gender_index = -1
    age_index = -1
    fare_index = 1

    for columnIndex, column in enumerate(records[0]):
        if column == "Survived":
            survived_index = columnIndex
        elif column == "Pclass":
            Pclass_index = columnIndex
        elif column == "Name":
            name_index = columnIndex
        elif column == "Gender":
            gender_index = columnIndex
        elif column == "Age":
            age_index = columnIndex
        elif column == "Fare":
            fare_index = columnIndex

    Total = len(records[1])
    First = 0
    Second = 0
    Third = 0

    FirstSurvived = 0
    SecondSurvived = 0
    ThirdSurvived = 0


    for person in records[1]:
        if person[Pclass_index] == 1:
            First = First + 1
        elif person[Pclass_index] == 2 :
            Second = Second + 1
        elif person[Pclass_index] == 3 :
            Third = Third + 1


    for person in records[1]:
        if person[Pclass_index] == 1 and person[survived_index] == True:
            FirstSurvived = FirstSurvived + 1
        elif person[Pclass_index] == 2 and person[survived_index] == True:
            SecondSurvived = SecondSurvived + 1
        elif person[Pclass_index] == 3 and person[survived_index] == True:
            ThirdSurvived = ThirdSurvived + 1

    print(First,Second,Third)
    print(FirstSurvived,SecondSurvived,ThirdSurvived)

    FirstFormatted = round((First / Total)*100,1)
    SecondFormatted = round((Second / Total)*100,1)
    ThirdFormatted = round((Third / Total)*100,1)

    FirstSurvivedFormatted = round((FirstSurvived / First) * 100, 1)
    SecondSurvivedFormatted = round((SecondSurvived / Second) * 100, 1)
    ThirdSurvivedFormatted = round((ThirdSurvived / Third) * 100, 1)

    print(FirstFormatted, SecondFormatted, ThirdFormatted)
    print(FirstSurvivedFormatted, SecondSurvivedFormatted, ThirdSurvivedFormatted)
    array = []
    array.append("== 1st Class ==")
    firststars = round(FirstFormatted/5) * "*" + round((100-FirstFormatted)/5) * " "
    firstToAppend = "Total |{0}| {1}%".format(firststars,FirstFormatted)
    array.append(firstToAppend)

    firststars2 = round(FirstSurvivedFormatted / 5) * "*" + round((100 - FirstSurvivedFormatted) / 5) * " "
    firstToAppend2 = "Alive |{0}| {1}%".format(firststars2, FirstSurvivedFormatted)
    array.append(firstToAppend2)



    array.append("== 2nd Class ==")
    firststars3 = round(SecondFormatted / 5) * "*" + round((100 - SecondFormatted) / 5) * " "
    firstToAppend3 = "Total |{0}| {1}%".format(firststars3, SecondFormatted)
    array.append(firstToAppend3)

    firststars4 = round(SecondSurvivedFormatted / 5) * "*" + round((100 - SecondSurvivedFormatted) / 5) * " "
    firstToAppend4 = "Alive |{0}| {1}%".format(firststars4, SecondSurvivedFormatted)
    array.append(firstToAppend4)



    array.append("== 3rd Class ==")
    firststars5 = round(ThirdFormatted / 5) * "*" + round((100 - ThirdFormatted) / 5) * " "
    firstToAppend5 = "Total |{0}| {1}%".format(firststars5, ThirdFormatted)
    array.append(firstToAppend5)

    firststars6 = round(ThirdSurvivedFormatted / 5) * "*" + round((100 - ThirdSurvivedFormatted) / 5) * " "
    firstToAppend6 = "Alive |{0}| {1}%".format(firststars6, ThirdSurvivedFormatted)
    array.append(firstToAppend6)


    array = "\n".join(array)
    return array



# You can play around with your solution from within this block.
if __name__ == '__main__':
    print(visualize((
        ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
        [
            (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'female', 38, 71.2833),
            (True, 2, 'Flunky Mr Hazelnut', 'female', 18, 51.2),
            (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
        ]
    )))
