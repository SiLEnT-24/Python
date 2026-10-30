num = int(input("Enter a number "))

z=1

for i in range(1, num+1):
    for j in range(1,i+1):
        print(z, end=" ")
        z+=1

    print()