import time

s=time.time()

print("second ",s)

print(time.localtime(s))
print(time.gmtime(s))
print(time.ctime(s)) 