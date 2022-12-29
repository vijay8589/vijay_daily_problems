"""input : {‘a’: 100, ‘b’:200, ‘c’:300}
Output : 600

Input : {‘x’: 25, ‘y’:18, ‘z’:45}
Output : 88"""

def returnSum(myDict):
 
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
 
    return final
 
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))


#Using For loop to iterate through values using values() function


def returnSum(dict):
 
    sum = 0
    for i in dict.values():
        sum = sum + i
 
    return sum
 
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))


# Using values() and sum() function

def returnSum(dict):
    return sum(dict.values())
 
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))