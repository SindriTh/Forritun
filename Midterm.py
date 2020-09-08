############ Problem 1

number_to_multiply = int(input("Input number to multiply: ")) # Do not change this line
how_often = int(input("Input how often to multiply: ")) # Do not change this line

for i in range(1,how_often+1):
    print(i*number_to_multiply)







############ Problem 2

dog_age = int(input("Input dog's age: ")) # Do not change this line


if(dog_age == 1):
    human_age = 15
    print("Human age: ", human_age)
elif(1 < dog_age <= 16):
    human_age = 16
    print("Human age: ", human_age + 4*dog_age)
else:
    print("Invalid age")






############ Problem 3

import math

start_int = int(input("Input starting integer: "))

while(start_int >= 2):
    start_int = math.sqrt(start_int) 
    print(round(start_int,4))






############ Problem 4

max_int = int(input("Input max integer: "))

for i in range(1,max_int+1):
    for y in range(1, i+1):
        print(y, end=" ")
    print()