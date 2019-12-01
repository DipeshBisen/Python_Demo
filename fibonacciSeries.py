
def fib_fun(x):
    a=0
    b=1

    if x==1 :
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,x):
            c=a+b
            a=b
            b=c
            if c > x:
                break
            else:
                print(c)




fib_fun(100)