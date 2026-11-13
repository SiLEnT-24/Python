def swap():
    n = int(input("Enter a first number "))
    m = int(input("Enter a second number "))

    print("before swap ", "n ", n, "m ", m)
    c=n
    n=m
    m=c

    print("after swap","c ", c)

    #calling function 
swap()