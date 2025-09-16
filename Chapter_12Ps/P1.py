''' Write a program to open three file if any files are not print a msg without existing program '''
try:
  with open("1.txt" , "r") as f:
    print (f.read())

except Exception as e:
    print(e)
try:
  with open("2.txt" , "r") as f:
    print (f.read())

except Exception as e:
    print(e)
try:
   with open("3.txt" , "r") as f:
    print (f.read())
except Exception as e:
            print(e)
    
print("Thank you")