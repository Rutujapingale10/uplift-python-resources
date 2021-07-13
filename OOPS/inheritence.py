class Person:
    def __init__(self, fname, lname):
        self.first = fname
        self.last = lname

    def print_person_name(self):
        print(self.first, self.last)


class Student(Person):
    def __init__(self, fname, lname, yearofpassing):
        # there are two ways of calling the parent class's init object. one is using the normal ParentClassName.__init__(self,other paramteres)
        # Person.__init__(self, fname, lname)
        # the other option is calling the super fucntion, here you don't need to write the parent calss name as well as the self keyword
        super().__init__(fname, lname)
        self.gradyear = yearofpassing

    def showgradyear(self):
        print(self.gradyear)


X = Student("Sagnik", "Mitra", 2022)
X.showgradyear()
