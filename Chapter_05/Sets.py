# Set is a collection of non repetitivve elements 
#    1. it is immutable can't change the value  
#    2. it is an unordered.
#    3. it is an unindexed.
#    4. it can't contain duplicate values.

a = set() # empty set ,don't use s = {} for create empty set 
print(a,type(a))

m = {4,50,8,3,2,45,788,7}
n = {8,3,7,44,2,5}

# #  Operation of Sets

m.add(55) # add the value 
print(len(m)) # get the length of set
print(m.remove(2)) # remove the specific element 
print(m.union(n)) # get the element both set
print(m.intersection(n)) # common in the both set
print(m,type(m)) # set