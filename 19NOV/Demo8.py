#contact book
contactlist=[]
def addcontact():
    name=input("enter name ")
    address=input("enter address ")
    email_id=input("enter email id ")
    mobile=("enter mobile number ")

    data={"name":name, "address":address, "email_id":email_id, "mobile":mobile}

    contactlist.append(data)
    print("contact added ")

def display():
    if(len(contactlist)==0):
        print("record is not found ")

    else:
        print("===contact list===")
        for x in contactlist:
            print("name ", x["name"])
            print("address ", x["address"])
            print("Email_id ", x["email_id"])
            print("Mobile ", x["mobile"])
            print("=========================")

while True:
    print("1 for add contact")
    print("2 for display contact")
    print("0 for exist")

    ch=int(input("enter your choice "))

    if(ch==1):
        addcontact()

    elif(ch==2):
        display()
    
    elif(ch==0):
        break
