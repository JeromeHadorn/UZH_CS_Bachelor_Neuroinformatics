def read_csv(path):
    f = open(path)
    giantArray = []
    for line in f.readlines():
        line = line.strip()
       # print(line)
       # print(line.split(","))
        rowData = line.split(',')
        if line == "":
            continue
        #print(tuple(rowData))
        giantArray.append((tuple(rowData)))
    f.close()
    return giantArray

#print(read_csv("example.csv"))




def preprocess(records):

    header = None

    survived_index = -1
    Pclass_index = -1
    name_index = -1
    gender_index = -1
    age_index = -1
    fare_index = 1

    passengers = []
    for index, passenger in enumerate(records):
        if index == 0:
            header = passenger
            for columnIndex, column in enumerate(header):
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
        else:

            survived_passes_positive = ["Survived","Yes","yes","TRUE","True","true","survived","Alive","t","T"]
            survived_passes_negative = ["Dead","No", "no", "False","false","FALSE", "dead","DEAD", "f", "F","Survived=dead"]
            male_values = ["m","male","M","MALE","Male"]
            female_values = ["f","female","FEMALE","Female","F"]

            survived = None
            Pclass = None
            Name = None
            Gender = None
            Age = None
            Fare = None

            #Survived Check
            if passenger[survived_index] in survived_passes_positive:
                survived = True
            elif passenger[survived_index] in survived_passes_negative:
                survived = False
            else:
                #print("Survived - HORRIBLE DATA",passenger[survived_index])
                continue

            #Pclass
            if passenger[Pclass_index] == 1 or passenger[Pclass_index] == "1":
                Pclass = 1
            elif passenger[Pclass_index] == 2 or passenger[Pclass_index] == "2":
                Pclass = 2
            elif passenger[Pclass_index] == 3 or passenger[Pclass_index] == "3":
                Pclass = 3
            else:
                #print("Pclass - HORRIBLE DATA", passenger[Pclass_index])
                continue

            # Name
            if passenger[name_index] != "":
                Name = str(passenger[name_index])
            else:
                #print("Name - HORRIBLE DATA", passenger[passenger])
                continue

            #if '"' in passenger[name_index]:
                #print("TODOOO: - there are quotes", passenger[name_index])

            # Survived Check
            if passenger[gender_index] in male_values:
                Gender = "male"
            elif passenger[gender_index] in female_values:
                Gender = "female"
            else:
                #print("Gender - HORRIBLE DATA", passenger[gender_index])
                continue

            #Age Check
            try:
                float(passenger[age_index])
            except ValueError:
                #print("Not a float", passenger[age_index])
                continue


            floatValue = float(passenger[age_index])
            if 0.0 < floatValue < 100.0:
                Age = float(passenger[age_index])
            else:
                #print("Age - HORRIBLE DATA", passenger[age_index])
                continue


            #Fare Check
            floatFare = None
            try:
                float(passenger[fare_index])
                floatFare = float(passenger[fare_index])
            except ValueError:
                #continue
                #print("Fare Not a float",passenger[fare_index])
                floatFare = 25.0

            if 0.0 < floatFare:
                Fare = floatFare
            else:
                Fare = 25.0
                #print("Changed Fare",passenger[fare_index])


            array = [survived,Pclass,Name,Gender,Age,Fare]
            passengers.append(tuple(array))

    #print("header",header,survived_index,Pclass_index,name_index,gender_index,age_index,fare_index)
    return  (header,passengers)


a = preprocess(read_csv("titanic.csv"))



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
           # print()


    rateMenOver15 = None
    rateFemaleOver15 = None
    rateMenUnder15 = None
    rateFemaleUnder15 = None

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






    return ((rateMenUnder15,rateFemaleUnder15),(rateMenOver15,rateFemaleOver15))


b = survival_rates(a)

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

print(visualize(a))
