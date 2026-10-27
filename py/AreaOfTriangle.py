# When length of the side of the triangle is known- a,b,c
#semi perimeter = (a+b+c)/2
#area of triangle = sqrt(s*(s-a)*(s-b)*(s-c))

a=float(input("Enter length of side a: "))
b=float(input("Enter length of side b: "))
c=float(input("Enter length of side c: "))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle is:",round(area,2))