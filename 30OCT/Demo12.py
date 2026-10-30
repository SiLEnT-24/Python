#nested for loop
num = int(input("Enter a number "))

for i in range(1,num+1):
    #for space
    for k in range(num,i,-1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end= " ")
    print()