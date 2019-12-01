def fact(n):
    f=1

    for i in range(1,n+1):
        f=f*i
    return f

num=fact(4)
print(num)

import  sys
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())
def myfun():
    print("hello")
    myfun()
myfun()