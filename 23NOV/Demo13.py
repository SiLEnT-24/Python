#Inheritance - types: 1. single inheritance: one base class one drive class

class area:
    def seta(self):
        self.a=3.4
        return(self.a)
class circle(area):
    def display(self):
        self.r=area.seta(self)
        self.x=3.14*self.r*self.r
        print("area of circle ",self.x)

obj=circle()
obj.display()