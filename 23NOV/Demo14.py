#hierarchical inheritance : one base class and multiple derived classes


class area:
    def seta(self):
        self.a=3.4
        return(self.a)

    def setb(self):
        self.b=5.4
        return(self.b)

class circle(area):
    def display(self):
        self.r=area.seta(self)
        self.x=3.14*self.r*self.r
        print("area of circle ",self.x)
class rectangle(area):
    def demo(self):
        self.l=area.seta(self)
        self.b=area.setb(self)
        print("area of rectangle", self.l*self.b)

obj=circle()
obj.display()

obj1=rectangle()
obj1.demo()
