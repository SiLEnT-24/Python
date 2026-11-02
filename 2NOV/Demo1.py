# for unit conversion
print("press1 for km to meter")
print("press2 for meter to km")
print("press3 for faherenheit to celsius")
print("press4 for kilogram to gram")
print("press5 for gram to kilogram")

ch = int(input("Enter your choice: "))
value = float(input("Enter the value"))

if (ch==1):
    result = value*1000
    print("result= ", result)

elif (ch==2):
    result = value/1000
    print("result= ", result)

elif (ch==3):
    result = (value-32)*5/9
    print("result= ", result)

elif (ch==4):
    result = value*1000
    print("result= ", result)

elif (ch==5):
    result = value/1000
    print("result= ", result)