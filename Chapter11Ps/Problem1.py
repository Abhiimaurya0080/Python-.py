
# class TwoDVector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j")


# class ThreeDVector(TwoDVector):
#     def __init__(self, x, y, z):
#         super().__init__(x, y)   # initializes i and j from parent
#         self.k = z

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


# # Test the classes
# a = TwoDVector(4, 5)
# a.show()   # Output: The vector is 4i + 5j

# b = ThreeDVector(4, 5, 6)
# b.show()   # Output: The vector is 4i + 5j + 6k




class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)   # initializes i and j from parent
        self.k = z

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


# Test the classes
a = TwoDVector(4, 5)
a.show()   # Output: The vector is 4i + 5j

b = ThreeDVector(4, 5, 6)
b.show()   # Output: The vector is 4i + 5j + 6k

