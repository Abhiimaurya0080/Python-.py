''' write the python program to convert inches into cms'''
def inches_into_cms(inch):
    return inch * 2.54
n = int(input(" Enter your inches: "))
print(f"the Value is {inches_into_cms(n)}")