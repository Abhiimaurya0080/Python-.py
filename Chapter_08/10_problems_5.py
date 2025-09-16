# print the function name and its docstring using pattern 
def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n - 1)

# Call the function
pattern(3)
