#instance variables and class variables

#Namespace -->Class namespace and Instance namespace

class myClass:

    salary=2000 #Class namespace

    def __init__(self): # Object Namespace
        self.name="Raj"
        self.age=18

p1=myClass()
p2=myClass()

p1.name="Harsh" # instance variable

myClass.salary=3000  # class variable

print(p1.name, " ",p1.age," ", myClass.salary)
print(p2.name, " ",p2.age," ", myClass.salary)