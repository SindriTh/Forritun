import math

def valmynd():
    print("Please choose one of the options below:")
    print("a. Display the sum of the first N natural numbers. ")
    print("b. Display the sum of the first N Fibonacci numbers. ")
    print("c. Display the approximate value of e using N terms.")
    print("x. Exit from the program.")
    print()
    return


def isallowed(userinput):
    if(userinput == "a"):
        return True
    elif(userinput == "b"):
        return True
    elif(userinput == "c"):
        return True
    return False


def getoutstring(selected,inputnumber):

    if(selected == "a"):
        outputstring = "Natural number sum: {}".format(sum_natural(inputnumber))
    elif(selected == "b"):
        outputstring = "Fibonacci sum: {}".format(sum_fibonacci(inputnumber))
    else:
         outputstring = "Euler approximation: {}".format(approximate_euler(inputnumber))

    return outputstring
    


def sum_natural(n_int):

    if n_int >= 2:
        result = int(n_int*(n_int+1) / 2)
        return result



def sum_fibonacci(n_int):

    if n_int >= 2:

        fib_int_1 = 0
        fib_int_2 = 1
        result = 1

        for i in range(n_int-2):
            fib_int_3 = fib_int_1 + fib_int_2
            fib_int_1 = fib_int_2
            fib_int_2 = fib_int_3
            result += fib_int_3

        return result

def approximate_euler(n_int):
    if n_int >= 2:
        result = 1

        for i in range(1,n_int):
            result += 1/ math.factorial(i)

        return round(result,5)


option = ""
valmynd()
while option != "x":
    
    option = input("Enter option: ").lower()

    if isallowed(option):
        number = int(input("Enter N: "))
        outstring = getoutstring(option,number)
        print(outstring)
        print()

    elif(option != "x"):
        print("Unrecognized option ",option)
        valmynd()
