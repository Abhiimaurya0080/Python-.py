# write a recursive function to sum of calculate n numbers

'''
Sum(1) = 1 
Sum(2) = 1 + 2 
Sum(3) = 1 + 2 + 3 
Sum(4) = 1 + 2 + 3 + 4 
Sum(5) = 1 + 2 + 3 + 4 + 5
Sum(n) = 1 + 2 + 3 +......(n-1)+n
sum (n )= n + sum(n-1) 



'''
def sum (n):
    if n==1:
        return 1
    return n + sum(n-1)
# n = int(input("Enter a number: "))
# print(f"Sum of" {n} "number is:{(result)}")
print (sum(9))
