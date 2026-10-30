num = int(input("Enter your name "))

t = 1
i = 1
f = 0

while(i<=num):
     t = t*i
     i = i+1
     f = f + 1/t

print(f)