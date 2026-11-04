#count no. of words in a string

s = input("Enter a string: ")
print(s)
words = s.split(" ")
print("Number of words:", words, len(words))
countchar=0
count=0
for x in s:
    count+=1
    countchar+=len(x)
print("count", count,  "countchar", countchar)
