#for read a file
x=open("students.text","r")
# s=x.read(4)
# s=x.read()
# s=x.readline()     # read single top most list
s=x.readlines() # read data in list form
print("file content ", s)