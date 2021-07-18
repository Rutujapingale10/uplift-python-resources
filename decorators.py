"""
In python, functions are first class object that means that python fucntion can be used or passed as arguments

We can treat any fucntion as objects
"""


def changeToUpperCase(text):
    return text.upper()


print(changeToUpperCase("sagnik"))

myVar = changeToUpperCase
print(myVar('Hello'))


def upperVal(text):
    return text.upper()


def lowerVal(text):
    return text.lower()


def myFun(function):
    greeting = function("HIIII")
    print(greeting)


myFun(lowerVal)
