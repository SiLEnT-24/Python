rows=2
cols=3

arr=[]

for i in range(rows):
    row=[]
    for j in range(cols):
        value=int(input("Enter number:"))
        row.append(value)
    arr.append(row)

print(arr)