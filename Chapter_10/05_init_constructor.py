
'''__init__ constructor ---> special method which is first run as soon as object is created '''
 

class Employee:
    def __init__(self, name, salary, language, address, company):  # dunder method which auto called
        print("I am a cyber engineer")
        self.name = name
        self.salary = salary
        self.language = language
        self.address = address
        self.company = company

# Creating an object of Employee class
abhii = Employee("abhii", "2200000", "python", "singapore", "infosys")
abhii.language = "Javascript"  # This is instance Object 

# Printing the attributes of the instance
print(abhii.name, abhii.salary, abhii.language, abhii.address)
