SUM = "1"
PRODUCT = "2"
QUIT = "9"

def printchoices():
    print("1: Compute the sum of 1..n")
    print("2: Compute the product of 1..n")
    print("9: Quit")

def checkchoice(choice):    
    if choice == QUIT:
        return "Q"

    if choice == SUM:
        n_int = getvalidinput()
        if n_int != None:
            return calculatesum(n_int)

    elif choice == PRODUCT:
        n_int = getvalidinput()
        if n_int != None:
            return calculateproduct(n_int)
    return

def calculatesum(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

def calculateproduct(num):
    sum = 1
    for i in range(1,num+1):
        sum *= i
    return sum

def getvalidinput():
    n = input("Enter value for n: ")
    try:
        return int(n)
    except ValueError:
        return

answer = ""
while(answer != "Q"):
    printchoices()
    choice = input("Choice: ")
    answer = checkchoice(choice)
    if answer != None and answer != "Q":
        print("The result is: {}".format(answer))





#  DÆMI 2 ################################################################



# Reynir að opna skránna
def trytoopen(filename):
    try:
        file_obj = open(filename)
        return file_obj
    except FileNotFoundError:
        return

# Sækir top 2 nöfnin og breytir öllum tölum í intigers
def gettoptwo(obj):
    return obj[0:2]

# Breytir file object i lista
def objtolist(obj):
    namelist = []
    size = sum(1 for i in obj)
    obj.seek(0)
    for line in range(0,size):
        sublist = []
        for word in obj.readline().split():
            sublist.append(trytypetoint(word))
            
        namelist.append(sublist)
    return namelist

# Splittar listanum í stráka og stelpur
def splitlist(namelist):
    boys = []
    girls = []
    for sublist in namelist:
        boys.append(sublist[1:3])
        girls.append(sublist[3:5])
    return boys,girls

# Sækir top 5 nöfnin
def gettopfive(namelist):
    topfive= namelist[0:5]
    return topfive

# Breytir viðeigandi gildum í listanum í int
def trytypetoint(str):
    try:
        intiger = int(str)
        return intiger
    except ValueError:
        return str

# Telur heildarfjölda nafna í listanum
def totalfrequency(namelist):
    sum = 0
    for item in namelist:
        sum += item[1]
    return sum

# Finnur fyrstu 50%
def getrank(namelist,total):
    rankcounter = 0
    sum = 0
    while(sum < total/2):
        sum += namelist[rankcounter][1]
        rankcounter += 1
    return rankcounter

#Prentar allt
def printeverything(file_obj):
    namelist = objtolist(file_obj)
    toptwo = gettoptwo(namelist)
    print(str(toptwo))
    boys,girls = splitlist(namelist)
    print(gettopfive(boys))
    print(gettopfive(girls))
    print("Total frequency of boy names: {}".format(totalfrequency(boys)))
    print("Total frequency of girl names: {}".format(totalfrequency(girls)))
    print("50th percentile rank for boys: {}".format(getrank(boys,totalfrequency(boys))))
    print("50th percentile rank for girls: {}".format(getrank(girls,totalfrequency(girls))))


# Aðalforrit byrjar
filename = input("Enter file name: ")
file_obj = trytoopen(filename)
if file_obj != None:
    printeverything(file_obj)
else:
    print("File {} not found".format(filename))