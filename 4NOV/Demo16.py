s="python is a simple and easy to understand the code"

search=input("Enter a string to search: ")
x=s.find(search)
if x==-1:
    print("String not found")
else:
    print("String found at index", x)
