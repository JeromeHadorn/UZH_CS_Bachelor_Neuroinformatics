# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
def survival_rates(dataset):
    survived_index = -1
    Pclass_index = -1
    name_index = -1
    gender_index = -1
    age_index = -1
    fare_index = 1

    for columnIndex, column in enumerate(dataset[0]):
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

    peopleCount = len(dataset[1])


    under15Male = 0
    over15Male = 0
    under15Female = 0
    over15Female = 0

    survivedunder15Male = 0
    survivedover15Male = 0
    survivedunder15Female = 0
    survivedover15Female = 0

    print(survived_index,Pclass_index,name_index,gender_index,age_index,fare_index)


    for person in dataset[1]:
        if person[age_index] > 15 and person[gender_index] == "male":
            over15Male = over15Male + 1
        elif person[age_index] > 15 and person[gender_index] == "female":
            over15Female = over15Female + 1
        elif person[age_index] <= 15 and person[gender_index] == "male":
            under15Male = under15Male + 1
        elif person[age_index] <= 15 and person[gender_index] == "female":
            under15Female = under15Female + 1
            

    for person in dataset[1]:
        if person[age_index] > 15 and person[gender_index] == "male" and person[survived_index] == True:
            survivedover15Male = survivedover15Male + 1
        elif person[age_index] > 15 and person[gender_index] == "female" and person[survived_index] == True:
            survivedover15Female = survivedover15Female + 1
        elif person[age_index] <= 15 and person[gender_index] == "female" and person[survived_index] == True:
            survivedunder15Female = survivedunder15Female + 1
        elif person[age_index] <= 15 and person[gender_index] == "male" and person[survived_index] == True:
            survivedunder15Male = survivedunder15Male + 1

    print(under15Female,over15Female,under15Male,over15Male)
    print(survivedunder15Female, survivedover15Female, survivedunder15Male, survivedover15Male)
    print(under15Female + over15Female + under15Male + over15Male)
    print(survivedunder15Male + survivedunder15Female + survivedover15Female + survivedover15Male)

    rateMenOver15 = None
    rateFemaleOver15 = None
    rateMenUnder15 = None
    rateFemaleUnder15 = None

    print(peopleCount)
    if over15Male != 0:
        rateMenOver15 = survivedover15Male / over15Male
        rateMenOver15 = round(rateMenOver15 * 100, 1)
    if over15Female != 0:
        rateFemaleOver15 = survivedover15Female / over15Female
        rateFemaleOver15 = round(rateFemaleOver15 * 100, 1)
    if under15Male != 0:
        rateMenUnder15 = survivedunder15Male / under15Male
        rateMenUnder15 = round(rateMenUnder15 * 100, 1)
    if under15Female != 0:
        rateFemaleUnder15 = survivedunder15Female / under15Female
        rateFemaleUnder15 = round(rateFemaleUnder15 * 100, 1)





    print(rateMenOver15,rateFemaleOver15,rateMenUnder15,rateFemaleUnder15)

    return ((rateMenUnder15,rateFemaleUnder15),(rateMenOver15,rateFemaleOver15))

# You can play around with your solution from within this block.
if __name__ == '__main__':
    # Investigate the 'titanic.csv' file before you attempt a submission. You might
    # want to download the file to your machine and open it with the functions that
    # you have written in Task 1+2. The following example is not complete...
    print(survival_rates((
        ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
        [
            (True, '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'female', 38, 71.2833),
            (False, '3', 'Heikkinen Miss. Laina', 'female', 26, 7.925)
            # ...
        ]
    )))
