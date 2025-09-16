# #1 write  program  find the greatest number entered by the user --------->>>>>>>>>>>>.
# a1 = int(input("Enter the number1:"))
# a2 = int(input("Enter the number2:"))
# a3 = int(input("Enter the number3:"))
# a4 = int(input("Enter the number4:"))
# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest number a1: ",a1)
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Greatest number a2: " ,a2)
# elif(a3>a1 and a3>a2 and a3>a4): 
#     print("Greatest number a3: " ,a3)
# elif(a4>a1 and a4>a2 and a4>a3):
#     print("Greatest number a4: " , a4)


# 2  Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user------------>>>>>>
# marks1 =  int(input("Enter marks 1: "))
# marks2 =  int(input("Enter marks 2: "))
# marks3 =  int(input("Enter marks 3: "))
# #  check total percentage
# total_percentage =(100*(marks1 + marks2 + marks3))/300
# if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("you are pass",total_percentage) # you will pass when your score will be 120
# else:
#     print("You failed ,try again next year!",total_percentage) #you will fail ,when you will be not score 33 in each  subject .


# 3 A spam comment is defined as a text containing following keywords:---------->>>>>>>>>.
# p1 =  "Make a lot of money "
# p2 =  "buy now "
# p3 = "subscribe this "
# p4 = "click this "
# message = input("Enter your comment: ")
# if((p1 in message) or (p2 in message ) or (p3 in message )or (p4 in message)):
#     print ("this is a spam comment")

# else:
#     print("This comment is not spam ")



# 4 Write a program to find whether a given username contains less than 10 characters or not.-------->>>>>>>
# username =  input("Enter username: ")

# if(len(username)<10):
#     print("This username contain less than 10 char")
# else:
#     print("All is well")


#5 .Write a program which finds out whether a given name is present in a list or not.------------->>>>>>>>>>>>>>
l = ["Abhii", "Rahul" , "Aniv", "Anant"]
name  = input("Enter your name: ")
if(name in l):
    print ("congrats! your name in the list")
else:
    print (" Sorry! you are not in th list")