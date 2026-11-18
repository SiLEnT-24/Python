import time

s=time.time()

# print("second ",s)

# print(time.localtime(s))
# print(time.gmtime(s))
# print(time.ctime(s)) 

#x=time.strftime("%a")
# x=time.strftime("%A")
# x=time.strftime("%d")
# x=time.strftime("%m")
# x=time.strftime("%y")
# x=time.strftime("%Y")
# x=time.strftime("%b") # month in short
# x=time.strftime("%B") # month fullname
x=time.strftime("%A %d-%m-%y %H:%I:%S %p")

print(x)