#string with membership operator

s = "python is programming language "
search=input("Enter a string ")
res = search in s
print(res)
if(res):
    print("string found")

else:
     print("not found")