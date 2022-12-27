# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))


duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))


from collections import defaultdict
 
 
def default_val():
    return 0
 
 
# dict : maintain count of each element. with default value of key is 0
mydict = defaultdict(default_val)
 
l = [1, 2, 3, 2, 6, 3, 5, 3, 7, 8]
 
for i in l:
    if mydict[i] == 1:
        l.remove(i)
    else:
        mydict[i] = 1
 
print(l)


# using dict.fromkeys

input_list = [1, 2, 3, 2, 6, 3, 5, 3, 7, 8]
mylist = list(dict.fromkeys(input_list))
print(mylist)



# list comprehension

list1 = [1, 2, 3, 2, 6, 3, 5, 3, 7, 8]
mylist = [ list1[i] for i in range(len(list1)) if list1.index(list1[i]) == i]
print(mylist)