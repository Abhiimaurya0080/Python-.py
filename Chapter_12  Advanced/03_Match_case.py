
def local_state(state):
    match state:
        case "404":
            return "Lower class State"
        case "501":
            return "Languagical State"
        case "0061":
            return "Most Populated State"
        case _:
            return "Unknown State"
    
# print(local_state("404"))
# # print(local_state("501"))  
print(local_state("0061")) 


'''' This is match case statement which is similar to Switch statement '''  