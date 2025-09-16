'''Write a progrsm to display a/b where  a and b are integers. If b = 0 , dispaly infinte by handling the ZeroDivisionError'''
try:
    a = int(input("Enter a: "))
    b = int(input("Enter a: "))
    print(a/b)
except ZeroDivisionError as v:

 print("Infinite")     