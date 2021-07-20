def fibonacciGenFun(totalLimit):
    a, b = 0, 1
    while(a < totalLimit):
        yield a
        a, b = b, a+b


x = fibonacciGenFun(5)
for i in fibonacciGenFun(5):
    print(i)
