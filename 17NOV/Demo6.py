# Explicit type casting And inmplicit type casting : perform by user Ex int(), str(), float()
#Explicit type casting : perform by compiler itself Ex n=5 result=n/2
# Identity operator - is , is not
# membership operator - in , not in 
# list method - pop()-index and remove()-value
# dict method - pop()-keywise and popitem()- last element
# set - pop() , remove() and discard()

keys=["rollno","name","age"]
values=[101,"ram",10]
student =dict(zip(keys,values))
print(student)
student.update({"city":"indore"})
print(student)