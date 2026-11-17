#deep copy
import copy
a=[2,45,4,2,454]
print(a)
b=copy.deepcopy(a)
b[0]=1
print(b)
print(a)