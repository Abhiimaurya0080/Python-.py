'''
INSTACE ATTRIBUTES/ OBJECT ATTRIBUTES
 if we given input in the instance class attributes then  print instance attr. coz instance attr.  take higher prefrencce  '''



class Employee:
 name =  "abhii"
 salary = 20000
 language =  "Python"
 address =  "Singapore"

abhii = Employee ()
abhii.language = "Javascript" # This is instance Object 
print(abhii.name, abhii.salary, abhii.language, abhii.address ) # Creating an onject of employee class
