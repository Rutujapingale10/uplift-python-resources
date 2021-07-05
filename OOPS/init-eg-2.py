class address:
    def __init__(self):
        print(id(self))


object1OfAddress = address()
print(id(object1OfAddress))
objectOfAddress = address()
