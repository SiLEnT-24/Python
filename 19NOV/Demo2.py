#for create file
fp=open("myfile.text","w")
print(type(fp))
print("filename ",fp.name)
print("filemode ",fp.mode)
print("filestatus ",fp.closed)

data=input("Enter data in a file ")
fp.write(data)
print("file created")
fp.close()