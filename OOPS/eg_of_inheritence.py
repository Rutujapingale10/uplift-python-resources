class Person():
    def __init__(self, name, regid):
        self.name = name
        self.regid = regid

    def display(self):
        print("Hello, Parent Class Here")
        print(self.name)
        print(self.regid)

# Now lets create the child class


class Employee(Person):
    def __init__(self, name, regid, salary, role):
        super().__init__(name, regid)
        self.salary = salary
        self.role = role

    def display_emp(self):
        print("hello, child class here")
        print(self.salary)


parentClassObject = Person("Sagnik", "180020278185")
childClassObject = Employee("Sagnik", 180020278185, 5000, "SWE Intern")

parentClassObject.display()
childClassObject.display_emp()
