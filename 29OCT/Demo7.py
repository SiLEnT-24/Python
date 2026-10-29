#for armstrong number 153

n = int(input("Enter number "))
r=n
res = 0
temp=n

while(n!=0):
    a=n%10
    res=(a**3)+res
    n=n//10

if(temp==res):
    print(r,"is armstrong")
else:
    print(r,"is not a armstrong")