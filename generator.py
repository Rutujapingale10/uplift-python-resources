"""
A generator fucntion is defined like a normal fucntion, but whenever it needs to generate a value, it does it with the 'yield'

"""


def myGenFun():
    yield 1
    yield 2
    yield 35


for value in myGenFun():
    print(value)
