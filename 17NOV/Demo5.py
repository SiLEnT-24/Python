# copy
import copy
a=[[2,45,4],[3,5,6]]
print(a)
b=copy.copy(a)
b[0][0]=1
print(b)
print(a)