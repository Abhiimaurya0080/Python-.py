# A conditional expression (also known as a "ternary operator") is a simplified, single-line version of an if-else statement. Conditional expression template: expression_if_true if condition else expression_if_false

a = int(input("Enter your age:"))
#    If ,Else if , Elif, Else
if(a>=22):
    print("Your are above the age of consent")

elif(a==0):
    print("You are entering 0 which is not valid age ")

else:
    print("you are below the age of consent")

print("End of  program ")
