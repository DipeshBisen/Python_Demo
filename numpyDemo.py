import numpy as np
a=np.array([1,2,3,5],int)
print(a)
print(type(a))

arrb=np.array([[3,4,4,8],
              [5,6,9,0],
               [8,7,3,1]])


arrtemp=arrb.reshape(4,3)


print(arrb)
print(arrb.dtype)
print(arrtemp)

arr2=np.linspace(0,10,5)
print(arr2)
arr3=np.arange(0,15,5)
print("arange(x,y,z)")
print(arr3)

arr4=np.logspace(1,10,5)
print(arr4)
arr6=np.zeros(5,int)
print(arr6)