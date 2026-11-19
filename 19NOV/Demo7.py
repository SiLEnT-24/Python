# for read a file
import os

if(os.path.exists("myfile.text")):
    x=open("myfile.text","r")
    s=x.read()
    print("file content ",s)

else:
    print("file not found")