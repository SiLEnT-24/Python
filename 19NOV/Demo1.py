# # student marks processing

# students=[]   #empty list
# while True:
#     print("1 for add student")
#     print("2 for display")
#     print("0 for exit")

#     ch=int(input("Enter your choice "))

#     if(ch==1):
#         name=input("Enter your name ")
#         marks=[]
#         for x in range(3):
#             m=float(input("enter marks "))
#             marks.append(m)

#         total=sum(marks)
#         per=total/3

#         if(per>=60):
#             div="I Div"
#         elif(per>=45 and per>60):
#             div="II Div"
            
#         data1={
#             "name ":name,
#             "marks ":marks, 
#             "total ":total, 
#             "per ":per, 
#             "Div  ":div
#             }
#         students.append(data1)
#         print("record added ")

#     elif(ch==2):
#         if(len(students)==0):
#             print("no record found ")

#         else:
#             for x in students:
#                 print("/n name- ", x["name"])
#                 print("total marks- ", x["total"])
#                 print("per- ", x["per"])
#                 print("Div- ", x["div"])

#     elif(ch==0):
#         break
#     else:
#         print("invalid choice!!!!")
# Student Marks Processing

students = []  # Empty list

while True:
    print("\n1 for add student")
    print("2 for display")
    print("0 for exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        name = input("Enter student name: ")

        marks = []  # Empty marks list

        for x in range(3):
            m = float(input("Enter marks: "))
            marks.append(m)

        total = sum(marks)
        per = total / 3

        data1 = {
            "name": name,
            "marks": marks,
            "total": total,
            "per": per
        }

        students.append(data1)
        print("Record added successfully!")

    elif ch == 2:
        if len(students) == 0:
            print("No record found")
        else:
            for x in students:
                print("\nName -", x["name"])
                print("Marks -", x["marks"])
                print("Total marks -", x["total"])
                print("Percentage -", x["per"], "%")

    elif ch == 0:
        print("Program exited")
        break

    else:
        print("Invalid Choice")