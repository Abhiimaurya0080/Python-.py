#  find the greatest number in three value
def greatest(a ,b ,c):
    if (a>b and a>c ):
        return a
    elif (b>a and b>c ):
        return b
    elif (c>b and c>a ):
        return c
    
a = 45
b = 566
c = 156
print(greatest(a,b ,c))