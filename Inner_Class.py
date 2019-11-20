
class Student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
        self.lap=self.Laptop() # 1st way: creating object of inner class inside outer class  constructor

    def show(self):
        print(self.name,self.rno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.model="Ab522tx"

        def show(self):
            print(self.brand,self.model)

s1=Student("naveen",12)
s2=Student("Raj",13)

s1.show()
s2.show()
print(id(s1.lap))
print(id(s2.lap))

lap=Student.Laptop() #2nd way: creating object of inner class outside outer class provided that we use outer class name to call it.

lap2=s2.lap
lap2.brand="Lenovo"
s2.show()
