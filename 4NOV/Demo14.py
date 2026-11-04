#change string to immutable to mutable
#using join method

s = "hello"

list1=list(s)
list1[0]="v"
newstr= " ".join(list1)
print(newstr)