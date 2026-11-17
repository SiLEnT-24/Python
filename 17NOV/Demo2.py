#dynamic dictionary

product={}
print(type(product))
n=int(input("Enter the limit "))

for i in range(1, n+1):
    key=input("enter key ")
    value=input("enter the value ")
    product.update({key:value})
print(product)