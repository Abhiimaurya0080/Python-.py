
   # Tuples is a imutable datatypes in python  can't change the value of listed elements
# a = (1,7,5,6)
b = (8,5,9,2)
# print(type(a))

# method
#  we can count the place number of tuples
a = ( 1, 45 , 21.36, 342 , False, 78 ,"Roshan", 78, 54.6  )
c = a.count(45) # the place value of 45 = 1 .
print(c)

# repeat the element 
repeated = a*3 #  repeat  the element of a list 
print (repeated)
 
#  Add to tuples 
concatenated = a + b

print(concatenated) #add two tuples 

#  Min  and max value in list 
tuples = [(2, 3), (1, 4), (5, 0)]
print(min(tuples))  # Output: 1,4
print(max(tuples))  # Output: 5,0









