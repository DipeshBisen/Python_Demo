
class Person:
    def __init__(self):
        self.name="Navin"
        self.age=28

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

    def update(self):
        self.age=30

obj1=Person()
obj2=Person()

#obj1.update()

if obj1.compare(obj2):
    print("Same")

else:
    print("Not same")
