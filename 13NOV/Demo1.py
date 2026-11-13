#Grade calculator

name = input("Enter your name: ")
P=int(input("Enter physics marks: "))
C=int(input("Enter chemistry marks: "))
M=int(input("Enter maths marks: "))
TOTAL = P + C + M
percentage = TOTAL / 3

if percentage >= 90 and percentage <= 100:
    print("Grade A")

elif percentage >= 80 and percentage < 90:
    print("Grade B")

elif percentage >= 70 and percentage < 80:
    print("Grade C")

elif percentage >= 60 and percentage < 70:
    print("Grade D")

else:
    print("Grade F")
