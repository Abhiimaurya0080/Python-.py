# class Employee:
#     a = 1  # Class variable

#     @classmethod
#     def show(cls):
#         print(f"The value of a is {cls.a}")

# @property
# def name(self):
#  return f"{self.fname} {self.lname}"

# @name.setter
# def name(self, value):
#   self.fname = value.split(" ")[0]  
#   self.lname = value.split(" ")[1]   

# e = Employee()
#  # This creates an instance variable, doesn't affect class variable
# e.name = "Abhii Maurya"
# print(e.fname,e.lname)
# e.show()  # Still prints class variable

class Employee:
    a = 1  # Class variable

    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]  
        self.lname = value.split(" ")[1]   

# Create an instance of Employee
e = Employee()
e.a  = 46
e.name = "Abhii Maurya"  # Set the name using the setter
print(e.fname, e.lname)   # Print first and last name
e.show()  # Still prints class variable

