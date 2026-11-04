#string is palindrome or not

s = input("Enter a string: ")
res = ""
for i in s:
    res = i + res

print("Reverse of the string is: ", res)

if s == res:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.") 