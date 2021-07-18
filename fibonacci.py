#  1 1  2
#  a b a+b
# 0 1 1 2 3 5 8 13 21 34

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("What is this behaviour?")
    elif n == 0:
        print(a)
    elif n == 1:
        print(b)
    for i in range(1, n):
        c = a+b
        a = b
        b = c
    return b


usrInp = int(input("Enter which fibonacci number you want"))
print(fibonacci(usrInp-1))
