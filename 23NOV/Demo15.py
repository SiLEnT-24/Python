#multilevel inheritance

class base1:
    def seta(self):
        self.a=3.4
        return(self.a)
class derived1(base1):
    def setb(self):
        self.x=base1.seta(self)
        self.y=43
        return(self.x+self.y)
class derived2(derived1):
    def demo(self):
        self.total=derived1.setb(self)
        self.avg=self.total/2
        print("avg ",self.avg)

obj=derived2()
obj.demo()