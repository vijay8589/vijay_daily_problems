# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]


 
# Swap function
def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList
     
newList = [12, 35, 9, 56, 24]
print(swapList(newList))



def swapList(list):
     
    first = list.pop(0)  
    last = list.pop(-1)
     
    list.insert(0, last) 
    list.append(first)  
     
    return list
     

newList = [1, 2, 3]
 
print(swapList(newList))