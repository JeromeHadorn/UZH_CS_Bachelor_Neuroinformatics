import os


# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
def get_average_grade(path):
    
    numberOfGrades = 0
    summation = 0

    if not os.path.exists(path):
        return None
    else:
        f = open(path, 'r')
        for line in f.readlines():
            if ":" in line and "#" not in line:
                indexOfColon = line.find(':')
                stringGrade = line[indexOfColon+1:]
                stringGrade = stringGrade.strip()

                numberOfGrades += 1
                summation = summation + float(stringGrade)
               
        if numberOfGrades == 0:
            return 0.0
        else:
            return summation/numberOfGrades




# You can play around with your solution from within this block.
if __name__ == '__main__':
    print(get_average_grade("public/my_grades.txt"))
