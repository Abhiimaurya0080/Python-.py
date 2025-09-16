# Multiple Inheritance  in Python

class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(f"This is an employee of {self.company} and salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Here is your language {self.language}")

class Programmer(Employee, Coder):
    company = "Google Inc"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language}")
# Create objects
a = Employee("Alice", 50000)
b = Programmer("Bob", 70000)

# Calls
a.show()
b.show()
b.printLanguage()
b.showLanguage()
