def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
        
def getprimelist(listi):
    newlist = []
    for i in int_list:
        if is_prime(i) and i not in newlist:
            newlist.append(i)
    return newlist

def printstuff(int_list):
    print("Input list:",int_list)
    int_list.sort()
    print("Sorted list: ",int_list)
    primelist = getprimelist(int_list)
    print("Prime list: ",primelist)
    outstring = getminmaxavg(int_list)
    print("Min: {}, Max: {}, Average: {:.2f}".format(outstring[0],outstring[1],outstring[2]))
    
def getminmaxavg(int_list):
    minint = int_list[0]
    maxint = int_list[0]
    sum = 0
    for i in int_list:
        if i > maxint: maxint = i
        if i < minint: minint = i
        sum += i
    sum = sum/len(int_list)
    return minint,maxint,sum

def isoktoint(strlist):
    try:
        int_list = [int(i) for i in str_list]
    except ValueError:
        return False
    
    for i in str_list:
        if int(i) < 0:
            return False
    
    return True

# The main program starts here
str_list = input("Enter integers separated with commas: ").split(",")

if isoktoint(str_list):
    int_list = [int(i) for i in str_list]
    printstuff(int_list)
else:
    print("Incorrect input!")

    