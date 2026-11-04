#split string and convert to another format
s="2026-11-04"
print(s)

a = s.split("-")
print(type(a))
print(a)
s1=a[2]+"/"+a[1]+"/"+a[0]
print(s1)