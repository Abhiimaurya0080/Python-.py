a = 79 # global variable 
def fun():
    global a # to use global variable in function
    a = 9 # local variable 
    print(a)


fun()  
print(a)

