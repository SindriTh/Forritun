what_to_show = input("Input f|a|b (fibonacci, abundant or both): ")

if(what_to_show == "f" or what_to_show == "b" ):
    length = int(input("Input the length of the sequence: "))

    fib_int_1 = 0
    fib_int_2 = 1

    print("Fibonacci Sequence:")
    print("-------------------")
    print(fib_int_1)
    print(fib_int_2)

    for i in range(0,length-2):
            fib_int_3 = fib_int_1 + fib_int_2
            fib_int_1 = fib_int_2
            fib_int_2 = fib_int_3
            print(fib_int_3)


if(what_to_show == "a" or what_to_show == "b" ):
    length = int(input("Input the max number to check: "))

    print("Abundant numbers:")
    print("-----------------")

    for num in range(1,length+1):

        sum = 0

        for i in range(1,num+1):
            if(num % i == 0):
                sum += i

        if(num < sum):
            print(num)