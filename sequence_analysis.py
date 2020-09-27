import math
ROUNDTO = 4

# A function for turning the fileobject to a list
def filetolist(fileobject):

    outlist = []
    for line in fileobject.readlines():
        try:
            value = float(line)
            if value not in outlist:
                outlist.append(round(value,ROUNDTO))
        except ValueError:
            pass
    return outlist

# A function to find the cumulative sum
def cumsum(sequence):

    cumsumlist = []
    sum = 0
    for value in sequence:
        sum += value
        cumsumlist.append((round(sum,ROUNDTO)))
    return cumsumlist

# A function to find the median
def median(sequence):

    if not len(sequence) == 0:
        if len(sequence) % 2 == 0:
            # finds the two values in the middle and finds their average
            output = (sequence[math.floor((len(sequence))/ 2)-1] + sequence[math.ceil((len(sequence))/ 2)]) / 2
        else:
             # finds the value in the middle
            output = sequence[int((len(sequence)+1)/ 2) - 1]

        return (round(output,ROUNDTO))

    else:
        return ""

# A function that prints the screen output
def printlines(sequence):
    print()
    print("File {}".format(files))

    print("\tSequence:")
    print("\t\t",end="")
    print(*sequence, sep=" ", end=" \n")

    print("\tCumulative sum:")
    print("\t\t",end="")
    print(*cumsum(sequence), sep=" ", end=" \n")

    sequence.sort()
    print("\tSorted sequence:")
    print("\t\t",end="")
    print(*sequence, sep=" ", end=" \n")

    print("\tMedian:")
    print("\t\t{}".format(median(sequence)))



# The main program
filename = input("Enter filenames: ")

for files in filename.split():
    try:
        file_obj = open(files)
        numbers =filetolist(file_obj)
        printlines(numbers)
    except FileNotFoundError:
        print()
        print("File {} not found".format(files))