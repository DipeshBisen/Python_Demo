from array import *

vals=array('i', [5,8, 6, 7, 4])
vals.reverse()
print(vals)

newArr=array(vals.typecode,(a*a*a for a in vals))

for e in newArr:
    print(e)

i=0
while i<len(newArr):
    print(newArr[i])
    i+=1