def filetolist(fileobject):
    firstlist = []
    secondlist = []
    for line in fileobject.readlines():
        firstlist = []
        for values in line.split():
            firstlist.append(int(values))
        secondlist.append(firstlist)

    return secondlist

def calculatevector(vectorlst):
    calculated = []

    for i in range(0,len(vectorlst[0])):
        calculated.append(0)
        for vectors in vectorlst:
            calculated[i] += vectors[i]
    print(calculated)

filename = input("Enter filename: ")
file_obj = open(filename)
vectorlist =filetolist(file_obj)
print(str(vectorlist))
calculated = calculatevector(vectorlist)



