# pattern program

n = int(input("Enter the limit "))

for i in range(n,1,-1):
    if (i%2==0):                #even
        for j in range(1,i+1): #increasing order 
            print(j, end=" ")

        print()