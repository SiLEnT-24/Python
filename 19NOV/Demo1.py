# student marks processing

students=[]   #empty list
while True:
    print("1 for add student")
    print("2 for display")
    print("0 for exit")

    ch=int(input("Enter your choice "))

    if(ch==1):
        name=input("Enter your name ")
        marks=[]
        for x in range(3):
            m=float(input("enter marks "))
            marks.append(m)

        total=sum(marks)
        per=total/3
        if(per>=60):
            div="I Div"
        elif(per>=45 and per>60):
            div="II Div"
        data1={"name ":name, "marks ":marks, "total ":total, "per ":per, "Div  ":div}
        students.append(data1)
        print("record added ")

    elif(ch==2):
        if(len(students)==0):
            print("no record found ")
            
        else:
            for x in students:
                print("name ", x["name"])
                print("total marks ", x["total"])
                print("per ", x["per"])
                print("Div ", x["div"])

    elif(ch==0):
        break
    else:
        print("invalid choice!!!!")