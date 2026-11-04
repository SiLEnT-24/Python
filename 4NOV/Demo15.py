s = "hello"

list1=list(s)
list1[0]="v"
# newstr= " ".join(list1)
# print(newstr)
s="".join(list1)
print(s)

#replace string
newstr=s.replace("v","h")
print(newstr)
