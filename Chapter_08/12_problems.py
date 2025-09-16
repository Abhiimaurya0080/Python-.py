''' writw a python program to remove a given word ffrom list and strip '''
def rem(l, word):
    n = []
    for  item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n
        
l = ["apple" , "bango" , "oranga", "guava"]
print(rem(l , "a"))