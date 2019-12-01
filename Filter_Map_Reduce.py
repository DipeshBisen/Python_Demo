
def is_Even(n):   #  lambda n: n%2==0
    return n%2==0

def add_All(a,b):     #  lambda a,b:a+b,doubles
    return a+b

nums=[1,2,3,4,5,6,7,8,9,10]

#filter(function,sequence)
#evens1= list(filter(is_Even,nums)) #without lambda
evens2=list(filter(lambda n: n%2==0,nums))#with lambda

doubles=list(map(lambda n:n*2,evens2))

#to use "reduce(function,sequence)" we need to import functools module
import functools as ft
#sum=ft.reduce(add_All,doubles)
sum=ft.reduce(lambda a,b:a+b,doubles)

print(sum)
