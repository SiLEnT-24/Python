# to find middle among 3 numbers using function

def middle():
    n = int(input("Enter 1st the number "))
    m = int(input("Enter 2nd the number "))
    o = int(input("Enter 3rd the number "))

    if(n>m and n<o or n<m and n>o ):
        print(n,"is middle")

    if(m>n and m<o or m<n and m>o ):
        print(m,"is middle")

    if(o>n and o<m or o<n and o>m ):
        print(o,"is middle")

middle()