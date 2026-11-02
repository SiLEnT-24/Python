# for unit conversion
import sys
while True:
    print("press0 for exit")
    print("press1 for km to meter")
    print("press2 for meter to km")
    print("press3 for faherenheit to celsius")
    print("press4 for celsius to faherenheit")
    print("press5 for kilogram to gram")
    print("press6 for gram to kilogram")

    ch = int(input("Enter your choice: "))
    if(ch==0):
        sys.exit("thank you!!")

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
        result = (value*9/5)+32
        print("result= ", result, "F")

    elif (ch==5):
        result = value*1000
        print("result= ", result, "gram")

    elif (ch==6):
        result = value/1000
        print("result= ", result, "kg")

    else: 
        print("Invalid!!!!!")