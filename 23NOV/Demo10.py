#constructor is a special member fuction in python . constructor define by magic method __init__()
class product:
    def __init__(self):#default constructor
        self.qty=4
        self.price=30455
        print("total ",(self.qty*self.price))
p=product()
