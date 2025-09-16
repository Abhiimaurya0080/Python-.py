a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
   raise ZeroDivisionError("hey you cannot divide a number by zero")
else:
  print(a/b)

# a = int(input("Enter a number: "))
# b = int(input("Enter second number: "))

# if b == 0:
#     raise ZeroDivisionError("Hey, you cannot divide a number by zero")
# else:
#     print(a / b)
