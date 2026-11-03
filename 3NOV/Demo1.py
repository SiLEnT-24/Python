#find duplicate data list/remove

a = [10, 20, 30, 45, 64,]
print(a)

b=[]

for x in a:
    if x not in b:
        b.append(x)

print("unique data")
print(b)