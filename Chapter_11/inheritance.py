'''Inheritance is th way to create a new class from derived classes.'''
class Employee:
      company = "Google"
      def show(self):
            print(f"This is an employee of{self.company} and salary is {self.salary}")
'''class Programmer(Employee):
       company = "infosys"
       def show(self):
              print(f"This is an employee of{self.company} and salary is {self.salary}")
def showlanguage(self):
            print(f"The name is{self.name}and he is good with{self.language}")'''

# upper this line of code is overwriting bcz its to tuff and thoose work do in short code


class Programmer(Employee):
      company = "Google inc  "
      def showlanguage(self):
            print(f"The name is{self.name}and he is good with{self.language}")


a = Employee()
b = Programmer()

print(a.company, b.company)