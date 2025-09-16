class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Freelancer(Programmer):
    c = 3

o = Employee()
print(o.a)#print the a attributes
# print(o.b) show an error as there is no b attributes in employee class

o = Programmer()
print(o.a ,o.b)

o = Freelancer()
print(o.a, o.b ,o.c)