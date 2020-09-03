n = int(input("Enter the length of the sequence: ")) # Do not change this line

num_int_1 = 0
num_int_2 = 1
num_int_3 = 2
print(num_int_2)
if(n > 1):
    print(num_int_3)
sum_last3= num_int_1 + num_int_2 + num_int_3
for i in range(1,n-1):
    num_int_4 = num_int_3 + num_int_2 + num_int_1
    num_int_1 = num_int_2
    num_int_2 = num_int_3
    num_int_3 = num_int_4
    print(num_int_4)
    
    
