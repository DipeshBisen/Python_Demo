from array import *
arr=array('i',[])

n=int(input("Enter size of array"))

for i in range(n):
    x=int(input("Enter element in Array"))
    arr.append(x)

print(arr)

for i in arr:
    print(i)
