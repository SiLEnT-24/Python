list1=[1, 2, 3, 4, 5]
list2=[6, 7, 8, 9, 10]

list3 = list2.copy()
print("list3 ", list3)

list1.append(100)
print("list1 after append ", list1)

del list1
print("list1 after delete ")