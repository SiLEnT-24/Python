#function with passing arguments
class product:
    def setdata(self,a,b,c,d):
        self.code=a
        self.name=b
        self.qty=c
        self.price=d
    def display(self):
        print("code ",self.code)
        print("name ",self.name)
        self.total=self.qty*self.price
        print("total price ",self.total)

obj1=product()
obj1.setdata(101,"printer",2,20000)
obj1.display()

obj2=product()
obj2.setdata(102,"pen",2,2000)
obj2.display()
