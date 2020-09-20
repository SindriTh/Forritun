import math

NATURAL = "a"
FIBONACCI = "b"
EULER = "c"
EXIT = "x"

# Prentar Valmynd
def valmynd():
    print("Please choose one of the options below:")
    print("a. Display the sum of the first N natural numbers. ")
    print("b. Display the sum of the first N Fibonacci numbers. ")
    print("c. Display the approximate value of e using N terms.")
    print("x. Exit from the program.")
    print()
    return

# Athugar hvort notandi hafi slegið inn löglegt input
def isallowed(userinput):
    if(userinput == NATURAL):
        return True
    elif(userinput == FIBONACCI):
        return True
    elif(userinput == EULER):
        return True
    return False

# Býr til streng til þess að prenta út frá reikniföllum
def getoutstring(selected,inputnumber):

    if(selected == NATURAL):
        outputstring = "Natural number sum: {}".format(sum_natural(inputnumber))
    elif(selected == FIBONACCI):
        outputstring = "Fibonacci sum: {}".format(sum_fibonacci(inputnumber))
    else:
         outputstring = "Euler approximation: {}".format(approximate_euler(inputnumber))

    return outputstring
    
# Reiknifall náttúrulega talna
def sum_natural(n_str):

    n_int = int(n_str)
    if n_int >= 2:
        result = int(n_int*(n_int+1) / 2)
        return result

# Reinkifall Fibonacci 
def sum_fibonacci(n_str):

    n_int = int(n_str)
    if n_int >= 2:

        fibonacci_int_1 = 0
        fibonacci_int_2 = 1
        result = 1

        for i in range(n_int-2):
            fibonacci_int_3 = fibonacci_int_1 + fibonacci_int_2
            fibonacci_int_1 = fibonacci_int_2
            fibonacci_int_2 = fibonacci_int_3
            result += fibonacci_int_3

        return result

# Reiknifall Euler
def approximate_euler(n_str):

    n_int = int(n_str)
    if n_int >= 2:
        result = 1

        for i in range(1,n_int):
            result += 1/ math.factorial(i)

        return round(result,5)


# Aðal keyrsla forritsins

option = ""
valmynd()
while option != EXIT:

    option = input("Enter option: ").lower()

    if isallowed(option):
        number = input("Enter N: ")
        outstring = getoutstring(option,number)
        print(outstring)
        print()

    elif(option != EXIT):
        print("Unrecognized option ",option)
        valmynd()
