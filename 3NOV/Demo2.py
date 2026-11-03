#linear or sequential searching

a = [1, 3, 4, 45, 53, 6, 2]
print(a)
found= 0
s=int(input("Enter data to be search "))
for i in range(0, len(a)):
    if(a[i]==s):
        found=1
        break
if(found == 1):
    print("element found at ", (i+1), "position")
else:
    print("element not found ")