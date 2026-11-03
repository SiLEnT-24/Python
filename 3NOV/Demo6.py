#slicing in list
a = [10, 20, 30, 40, 50, 60, 70, 80]
print(a[::]) #print all data
print(a[2::]) #print index 2 all
print(a[-5:-3:]) #print index -5 to -3
print(a[0:5:2]) #print index 0 to 5 with step 2
print(a[::-2]) #print all data in reverse order

del a[0:3] #delete index 0 to 3
print(a)