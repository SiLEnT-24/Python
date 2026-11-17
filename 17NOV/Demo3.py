#remove duplicate element from list
a=[11,13,24,54,646,11,13]
print(a)
x=list(dict.fromkeys(a))
print(x)
print(type(x))