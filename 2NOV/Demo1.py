# for unit conversion
print("press1 for km to meter")
print("press2 for meter to km")
print("press3 for faherenheit to celsius")
print("press4 for kilogram to gram")
print("press5 for gram to kilogram")
print("press6 for exit")

ch = int(input("Enter your choice: "))
value = float(input("Enter the value "))

if (ch==1):
    result = value*1000
    print("result= ", result, "meter")

elif (ch==2):
    result = value/1000
    print("result= ", result, "km")

elif (ch==3):
    result = (value-32)*5/9
    print("result= ", result, "°C")

elif (ch==4):
    result = value*1000
    print("result= ", result, "gram")

elif (ch==5):
    result = value/1000
    print("result= ", result, "kg")

elif (ch==6):
    print("Exit")

else: 
    print("Invalid!!!!!")