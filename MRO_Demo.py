
class A:
    def fun(self):
        print("A fun")

class B(A):
    pass

class C(A):
    def fun(self):
        print("C fun")


class D(B,C):
    pass

obj=D()
obj.fun()