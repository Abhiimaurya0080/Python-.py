dict1 = {'a': 1 ,'b': 2}
dict2 = {'a': 3 ,'c': 4}
dict2.update(dict1)
print(dict2) # dict2 is updated with dict1 values 

merged_dict = dict1 | dict2
print(merged_dict) # newm dict which is merged of dict1 and dict2
