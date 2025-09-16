try:
    a = input("Hey, enter your number : ")
    print(a)
except Exception as e:
    print(e)
finally:
    print("Thank you , I am in finally block ")