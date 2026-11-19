#for create file
fp=open("myfile.text","a")
data=""" python is a programming language it is easy to understand 
if the you by mistakely make a error the you don't find the error
"""
fp.write(data)
print("file created")
fp.close()
print("file status ", fp.closed)