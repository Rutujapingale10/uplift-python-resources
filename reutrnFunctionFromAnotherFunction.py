def createAdditionFunction(x):
    def insideAddition(y):
        return x+y

    return insideAddition


add_3_to = createAdditionFunction(3)
print(add_3_to(10))

print((createAdditionFunction(3))(10))
