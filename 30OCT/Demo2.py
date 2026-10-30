n = int(input("Enter a number"))

for i in range (1, n+1):
    print(i, end = " ")


for i in range(1,11):
    # if(i==6):          //print 1 to 5
    # if(i==6 and i ==9): //print 1 to 10
    if(i==6 or i ==9):   //print 1 to 5
        break
    print(i, end=" ")

print("loop is ended!!!!!")