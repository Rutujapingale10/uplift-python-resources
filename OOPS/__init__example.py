"""
The init fucntion is alwasy executed when a certain class is initaited
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Sagnik", 23)
print(p1.name)
print(p1.age)
