class myClass:
    def __init__(self, roll=12, section="X"):
        self.roll = roll
        self.section = section
        self.chant = "Jai Shree Ram"

    def printMyDetails(self):
        print(f"My roll is {self.roll}")
        print("My section is"+self.section)

    def myChant(self):
        print(self.chant)


"""
There is something called Default Parameter, if there is a paramter but still someone forget to add it, then the program by default take the deafult pararmter
"""
object1 = myClass(12, "C")
object1.printMyDetails()

object2 = myClass(11, "A")
object2.printMyDetails()


object3 = myClass(9, "D")
object3.myChant()

object4 = myClass("134", "LF")
object4.printMyDetails()
