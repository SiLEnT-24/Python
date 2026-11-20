try:
    x=open("student.text","r")
    # s=x.read(4)
    # s=x.read()
    # s=x.readline()     # read single top most list
    s=x.readlines() # read data in list form
    print("file content ", s)
except FileNotFoundError:
   print("file does not found")