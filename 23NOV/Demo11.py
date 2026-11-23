class product:
    def __init__(self,x,y):#parameterized constructor
        self.qty=x
        self.price=y
        print("total ",(self.qty*self.price))
obj1=product(2,20000)
obj2=product(2,40000)
