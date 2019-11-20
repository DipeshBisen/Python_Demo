
class Student:

    #class variable
    school="GNHS"

    def __init__(self,m1,m2):
        #instance variable
        self.m1=m1
        self.m2=m2

    # instance method
    def avg(self):
        return (self.m1+self.m2)/2

    #getter for m1
    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1=value

    #class method
    @classmethod
    def getSchool(cls):
        return cls.school


    #static method
    @staticmethod
    def info():
        print("This is static method")

s1=Student(80,90)
s2=Student(60,70)

s1.m1=100

print(s1.avg())
print(Student.getSchool())

#Calling static method
Student.info()
