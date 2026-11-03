# list with membership operator
a = [10, 20, 30, 40, 50, 60, 70, 80]
s=int(input("enter data to be search "))
res = s in a

if(res):
    print("data found")
else:
    print("data not found")