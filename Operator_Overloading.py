
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        if m1>m2:
            return True
        else:
            return False

    def __str__(self):
        return "{} {}".format(self.m1, self.m2)  # here we need to return marks in string format



s1=Student(60,95)
s2=Student(45,85)

#----------------------__add__(self,other)--------Or-----__sub__(self,other)--------------------------

s3=s1+s2
s4=s1-s2
print(s3.m1,s3.m2)
print(s4.m1,s4.m2)

#----------------------__gt__(self,other)---------------------------------------
if s1 > s2:
    print("S1 wins")
else:
    print("S2 wins")

#----------------------__str__(self,other)---------------------------------------
num1=5
# :)  __str__() method is overriden in int class
print(num1)

print(num1.__str__())  #internally it is

print(s1.__str__())
print(s1)  #we have overriden __str__() method for Student class
