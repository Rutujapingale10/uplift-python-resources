def myGenFun():
    yield 1
    yield 2
    yield 3
    yield 4


obj = myGenFun()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
