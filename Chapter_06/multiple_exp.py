a = int(input("Enter your age: "))
if(a%2==0):
    print("a is even")
if(a>=22):
    print("Your are above the age of consent")
    print("Good for you")

# In ladder we create more than 'elif' statement in expression
elif(a==0):
    print("You are entering 0 which is not valid age ")
elif(a>0):
    print("You are entering  not valid age ")

else:
    print("you are below the age of consent")

    print("End of  program ")
