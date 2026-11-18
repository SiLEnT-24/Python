#arbitary arguments list function

def addition(*x):
    print(type(x))
    print(sum(x))

addition(10)
addition(10,24)
addition(10,34,45)
addition(10,66,64,34)