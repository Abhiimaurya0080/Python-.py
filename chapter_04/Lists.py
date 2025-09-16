#  Lists are containers to store set of value of any data types
#  list is mutable function means  we can change the value of any  element int the list 
#           0         1      2     3       4      5      6
# text = [ "Alpaha", "Beta","Rajni", 55  , 554.55 ,457,  9899]
# print(text[0]) # Alpha
# text[0]= "Tangent"# change the value  of any element 
# print(text[0])
List = [1,2,54,64,21,3,79]
#    some types of list used in adv. function
List.sort()
print(List) # arrange in ascending order

List.reverse() # arrange in descending order
print(List)

List.append(000)
print(List) # add the value in the last of the element 

List.insert(6,5)
print(List) # add the value at specific postion , here 6 position and 5 value 

List.pop(5)
print(List) # remove the value  of place as number 


