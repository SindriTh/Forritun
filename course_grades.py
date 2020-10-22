# Tries to open the file
def openfile(filename):
    ''' This function accepts a filename and tries to open it, returns error if it can't '''
    try:
        obj = open(filename)
        return obj
    except FileNotFoundError:
        print("File {} not found".format(filename))
        return

# Creates a list from the weight file object
def weightobj2list(fileobj):
    ''' This function accepts a file object and returns a list (Specifically made for weights)'''
    weightlist = []

    for line in fileobj:
        for i in range(len(line.split())):
            if len(weightlist) != len(line.split()):
                weightlist.append([])
            weightlist[i].append(tryfloat(line.split()[i]))
    
    for i in range(len(weightlist)):
        weightlist[i] = tuple(weightlist[i])

    return weightlist

# Creates a list from the grade file object
def gradeobj2list(fileobj):
    ''' This function accepts a file object and returns a list (Specifically made for grades)'''
    studentlist = []
    for line in fileobj.readlines():
        studentgrades = []
        for grade in range(1, len(line.split())):
            studentgrades.append(tryfloat(line.split()[grade]))
        studentlist.append(tuple((line.split()[0],studentgrades)))

    return studentlist

# Tries to return the input string as a float
def tryfloat(string):
    ''' This function tries to return a string as a float, if it can't it returns a string'''
    try:
        temp = float(string)
        return temp
    except ValueError:
        return string

# Gets each student's average
def getaverage(student,weight):
    ''' This function gets the average from a list of grades and weights'''
    grades = student[1]
    average = 0
    for grade in range(len(grades)):
        average += grades[grade] * weight[grade][1]
    return average

# Prints the final justified list
def printfinal(grade,weight):
    ''' This function prints the final table of grades'''
    print()
    print("{:>16}{:>14}{:>14}{:>14}{:>14}{:>14}{:>14}".format("Student ID",weight[0][0],weight[1][0],weight[2][0],weight[3][0],weight[4][0],"Course grade"))
    for student in grade:
        print("{:>16}{:>14}{:>14}{:>14}{:>14}{:>14}{:>14}".format(student[0],*student[1],round(student[2],2)))

# Gets filename for weight and outputs a list
def getweightlist():
    ''' This function gets a filename from the user and returns the appropriate list (Specifically made for weights)'''
    weightfilename = input("Enter filename for parts: ")
    weight_obj = openfile(weightfilename)
    if weight_obj == None:
        return
    weightlist = weightobj2list(weight_obj)
    return weightlist

# Gets filename for grades and outputs a list
def getgradelist():
    ''' This function gets a filename from the user and returns the appropriate list (Specifically made for grades)'''
    gradefilename = input("Enter filename for grades: ")
    grade_obj = openfile(gradefilename)
    if grade_obj == None:
        return
    gradelist = gradeobj2list(grade_obj)
    return gradelist


#The main function.
def main():
    ''' The main function '''
    weight_list = getweightlist()
    if weight_list == None:
        return
    print(weight_list)

    grade_list = getgradelist()
    if grade_list == None:
        return
    print(grade_list)
    for studentindex in range(len(grade_list)):
        grade_list[studentindex] += getaverage(grade_list[studentindex],weight_list),

    print(grade_list)
    
    printfinal(grade_list,weight_list)

# Runs the main function on start
main()

