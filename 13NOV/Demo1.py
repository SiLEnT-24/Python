#Grade calculator

name = input("Enter your name: ")
P=int(input("Enter physics marks: "))
C=int(input("Enter chemistry marks: "))
M=int(input("Enter maths marks: "))
TOTAL = P + C + M
percentage = TOTAL / 3
grade = 0 
if percentage >= 90 and percentage <= 100:
    grade = "A"

elif percentage >= 80 and percentage < 90:
    grade = "B"

elif percentage >= 70 and percentage < 80:
    grade = "C"

elif percentage >= 60 and percentage < 70:
    grade = "D"

else:
    grade = "F"

print(f"Student: {name}")
print(f"Physics: {P}")
print(f"Chemistry: {C}")
print(f"Maths: {M}")
print(f"Total Marks: {TOTAL}")
print(f"Percentage: {percentage}")
print(f"Grade: {grade}")
