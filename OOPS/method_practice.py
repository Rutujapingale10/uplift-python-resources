class Chocolate:
    # initialization fucntion / Constructor
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    # a basic method
    def __desc__(self):
        return {
            f"This is {self.brand}'s {self.name}. This is price at {self.price} Rupees"
        }

    def __price__(self):
        return self.price

    def __nameOfProd__(self):
        return self.name


choco1 = Chocolate("KitKat", "Nestle", 120)
print(choco1.__desc__())
