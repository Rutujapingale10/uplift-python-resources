"""
An OOPL is basically Object Oriented Programming Language
Concepts we will learn under OOPS
* Class
* Object
* Method
* Encapsulation
* Inheritence
* Polymorphism
* Data Abstraction

Let's say I am a student. So what are my object?
email-id
registration-number
name
age
semester

class Student:
    there are these objects

# If mobile phone is a class, then Realme X2 Pro, Iphone 12 Pro MAx
all the phone objects has a camera, has a battery, has a processor, has a back panel
iPhone 12 Pro Max - LIDAR (this is this particular phone's own feature but it shares a list of properties with all the phone in the world)

"""


class sagnik:
    def __init__(self):
        # init means the initialization, getting familiar with the method
        # Here what it did, it defined my property
        self.name = "SagnikMitra"

    def print_name(self):
        print(self.name)


class Sagnik:
    # This is the default init method and whenever we define a class and create its object by calling later, this "init" is called by default
    def __init__(self):
        # init means the initialization, getting familiar with the method
        # Here what it did, it defined my property
        self.name = "SagnikMitra"

    def print_name(self):
        print(self.name)


"""
How to create an Object, basically we just need to call the class and the object is created but if it has some paramter that we will dicsuss right after now, those parameters are passed.
"""
obj = Sagnik()
obj2 = Sagnik()
obj.print_name()
