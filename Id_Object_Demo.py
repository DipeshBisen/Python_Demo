def myFuc(x):
    print("x=",id(x))
    x=6
    print(id(x))

a=5
print(id(a))
myFuc(a)

p=[4,5]
q=[4,5]
print(id(p))
print(id(q))
print(p == q)


