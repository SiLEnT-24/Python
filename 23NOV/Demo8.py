class product:
    def setdata(self):
        self.code=101
        self.name="printer"
        self.qty=4
        self.price=30455
    def display(self):
        print("code ",self.code)
        print("name ",self.name)
        self.total=self.qty*self.price
        print("total price ",self.total)

obj=product()
obj.setdata()
obj.display()