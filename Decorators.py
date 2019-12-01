import fibonacciSeries as fbc

b=fbc.fib_fun(100)  #importing mudules
print(b)
#---------------------------------------------------------------------------

def div(a,b):
    return a/b
#this "smart_div(func)"  decorator function can add additional features to existing "div(a,b)" function
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)

    return inner

div=smart_div(div)

ans=div(16,4)

print(ans)

