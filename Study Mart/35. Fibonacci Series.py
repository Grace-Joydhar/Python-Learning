def fibo(x):
    a= 0
    b= 1
    print(a)
    print(b)
    for i in range(2, x):
        c = a+b
        b, a = c,b
        print(c)
fibo(10)