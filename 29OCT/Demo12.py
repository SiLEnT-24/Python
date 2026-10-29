#check for leap year

yrs = int(input("Enter the year "))

if(yrs%400 == 0):
    print("This is leap year")

elif(yrs%4 == 0):
    print("This is leap year")

else:
    print("This is not a leap year")