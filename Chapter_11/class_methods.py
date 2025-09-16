'''directly related to class and not to instance of the class'''
class Employee:
    a = 1  # Class variable

    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")


Employee.show()


e = Employee()
e.a = 45  # This creates an instance variable, doesn't affect class variable
print(f"The value of instance variable a is {e.a}")
Employee.show()  # Still prints class variable

