 
''' Static Method --> this is a decorator it has not used to object '''

class Employee:
 name =  "abhii"
 salary = 2200000
 language =  "Python"
 address =  "Singapore"

 def getInfo(self):
  print(f"The lannguage is {self.language} The salary is {self.salary}")

 @staticmethod
 def greet():
   print("Good evening")

abhii = Employee ()
abhii.language = "Javascript" # This is instance Object 
abhii.getInfo() # This is equal to employee.getInfo(abhii)
abhii.greet()


