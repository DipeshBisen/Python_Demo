class A:
    def fun(self):
        print("fun parent")

    def __init__(self,n1):
        print("paremeterized parent")

class B(A):
    def __init__(self,num):
        super().__init__(num)
        print("param cons child")

    def callfun(self):
        super().fun()
        print("call function")


#------------------------------------------------------#
obj=B(4)
obj.callfun()
#print(obj.z)

