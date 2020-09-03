length = int(input("Input the length of series: "))

sum=0
for i in range(1,length+1):
    sum += 2*i * -(-1)**i
    print(2*i * -(-1)**i)
print("Sum: ",sum)