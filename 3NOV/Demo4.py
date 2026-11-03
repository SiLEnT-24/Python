#bubble sorting
a = [5, 4, 6, 7, 8, 2, 3]

print("before sorting")
print(a)

n=len(a)

for i in range(n):
    for j in range(n-2,-1, -1):   #data comparsion
        if(a[j]>a[j+1]):
            #swap
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print("sorted list ")
print(a)