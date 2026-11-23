class product:
    def __init__(self,x,y): #constructor and destructor
        self.qty=x
        self.price=y
        print("total ",(self.qty*self.price))
    def __del__(self):
        print("destructor called")
obj1=product(2,20000)
obj2=product(2,40000)
