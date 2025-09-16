# class Nummber:
#     def __init__(self,n)  ->None:
#         self.n = n

#         def __add__(self,other):
#             return self.n + other.n
        
#         n = Number(1)
#         m = Number(2)

#         print(n + m ) # THis will calln.__add___(m) 



class Number:
    def __init__(self, n) -> None:
        self.n = n

    def __add__(self, other):
        return self.n + other.n

# Create instances of Number
n = Number(1)
m = Number(2)

# This will call n.__add__(m)
print(n + m)  # Output: 3

