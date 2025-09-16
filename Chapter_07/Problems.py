# # 1. Write a program to print multiplication table of a given number using for loop. --------->>>>>>>>>>>>
# n = int(input("Enter your number:"))
# for i in range(1,11):
#     print(f"{n} x {i}= {n*i}")



#     # 2.. Write a program to greet all the person names stored in a list ‘l’ and which starts with S. ----->>>>
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for name in l:
#     if(name.startswith("S")):
#        print(f"Hello{name}")


    # 3.1. Write a program to print multiplication table of a given number using for  while loop.------->>>>>>>
# n = int(input("enter your number: "))
# i=0
# while i<10:
#     i += 1
#     print(f"{n}x {i} = {n*i}")


    # 4. Write a program to find whether a given number is prime or not.------------->>>>>>>>>>>>>>>
# n = int(input("enter a number : "))
# for i in range (2 , n):
#     if (n%i) == 0:
#          print("Number is not prime ")
# else:
#  print("number is prime")


# 4. 7. Write a program to print the following star pattern. --------------------->>>>>>>>>>>>>
''' * 
*** 
***** for n = 3 '''
# n = int(input("enter yout number:"))
# for i in range (1, n+1):
#     print(" "*(n-1), end=" ")
#     print("*"*(2*i-1), end="")
#     print("")

# 8. Write a program to print the following star pattern:----------->>>>>>>>>>>>>>>
'''* 
  ** 
  ***      for n = 3'''
# n = int(input("enter yout number:"))
# for i in range (1, n+1):
#     print(" "*(n-1), end=" ")
#     print("*"*(i), end="")
#     print("")


# 9. Write a program to print the following star pattern.----------->>>>>>>>>>>>>> 
'''* * * 
   *   *   for n = 3 
   * * * '''
n = int(input("Enter your number: "))
for i in range (1 , n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*",end=" ") 
        print(" "*(n-2),end=" ") 
        print("*",end=" ") 
        print(" ")
# 10. Write a program to print multiplication table of n using for loops in reversed order------------>>>>>>>>>>>
# n = int(input("Enter your number: "))
# for i in range(1,11):
#     print(f"{n}x{11-i} = {n*(11-i)}")
