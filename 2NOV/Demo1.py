# for unit conversion
print("press1 for km to meter")
print("press1 for meter to km")
print("press1 for faherenheit to celsius")
print("press1 for kilogram to gram")
print("press1 for gram to kilogram")

ch = int(input("Enter your choice: "))
value = float(input("Enter the value"))

if (ch==1):
    result = value*1000
    print("result= ", result)

if (ch==2):
    result = value/1000
    print("result= ", result)
