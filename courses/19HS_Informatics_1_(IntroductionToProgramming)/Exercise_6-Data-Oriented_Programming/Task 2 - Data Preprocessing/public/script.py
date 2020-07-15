# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
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
                print("Survived - HORRIBLE DATA",passenger[survived_index])
                continue

            #Pclass
            if passenger[Pclass_index] == 1 or passenger[Pclass_index] == "1":
                Pclass = 1
            elif passenger[Pclass_index] == 2 or passenger[Pclass_index] == "2":
                Pclass = 2
            elif passenger[Pclass_index] == 3 or passenger[Pclass_index] == "3":
                Pclass = 3
            else:
                print("Pclass - HORRIBLE DATA", passenger[Pclass_index])
                continue

            # Name
            if passenger[name_index] != "":
                Name = str(passenger[name_index])
            else:
                print("Name - HORRIBLE DATA", passenger[passenger])
                continue

            #if '"' in passenger[name_index]:
                #print("TODOOO: - there are quotes", passenger[name_index])

            # Survived Check
            if passenger[gender_index] in male_values:
                Gender = "male"
            elif passenger[gender_index] in female_values:
                Gender = "female"
            else:
                print("Gender - HORRIBLE DATA", passenger[gender_index])
                continue

            #Age Check
            try:
                float(passenger[age_index])
            except ValueError:
                print("Not a float", passenger[age_index])
                continue


            floatValue = float(passenger[age_index])
            if 0.0 < floatValue < 100.0:
                Age = float(passenger[age_index])
            else:
                print("Age - HORRIBLE DATA", passenger[age_index])
                continue


            #Fare Check
            floatFare = None
            try:
                float(passenger[fare_index])
                floatFare = float(passenger[fare_index])
            except ValueError:
                #continue
                print("Fare Not a float",passenger[fare_index])
                floatFare = 25.0

            if 0.0 < floatFare:
                Fare = floatFare
            else:
                Fare = 25.0
                print("Changed Fare",passenger[fare_index])


            array = [survived,Pclass,Name,Gender,Age,Fare]
            passengers.append(tuple(array))

    #print("header",header,survived_index,Pclass_index,name_index,gender_index,age_index,fare_index)
    return  (header,passengers)


# You can play around with your solution from within this block.
if __name__ == '__main__':
    # Investigate the 'titanic.csv' file before you attempt a submission. You might
    # want to download the file to your machine and open it with the function that
    # you have written in Task 1. The following example is not complete...
    titanic = [
        ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
        ('no', '3', 'Braund Mr. Owen Harris', 'male', '22', '7.25'),
        ('no', '3', 'Braund Ms. Maria', 'Female', '22', ''),
        ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
        ('', '3', 'Vander Planke Miss. Augusta Maria', 'female', '', ''),
        ('Dead', '4', 'Lennon Mr. Denis', 'male', '13', '15.5')
        # ...
    ]

    print(preprocess(titanic))
