#exception handling
try:
    n=5
    # res=n/0
    res=n/3
    print(res)
except ZeroDivisionError:
    print("no. must be > zero")
print("test program")