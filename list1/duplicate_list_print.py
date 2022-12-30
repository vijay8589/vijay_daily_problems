# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]
# Input :  list = [-1, 1, -1, 8]
# Output : output_list = [-1]


list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

uniqueList = []
duplicateList = []
 
for i in list:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
 
print(duplicateList)


