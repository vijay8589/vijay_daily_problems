# clear method Remove all elements from the list:

a = [10, 11, 12, 13, 12, 15]
a.clear()
print(a)


#pop()	 Removes and returns the last value from the List or the given index value.

a = [10, 11, 12, 13, 12, 15]
print(a.pop(0), a)


# using *=0 

a = [10, 11, 12, 13, 12, 15]
a *= 0
print(a)

# list re-instilation

a = [10, 11, 12, 13, 12, 15]
a = []
print(a)

# Python List remove() is an inbuilt function in the Python programming language that removes 
# a given object from the List. 

list1 = [ 1, 2, 1, 1, 4, 5 ]
list1.remove(1)
print(list1)



# removing duplicates 
list2 = [ 'a', 'b', 'c', 'd', 'd', 'e', 'd' ]
 
# removing 'd'
list2.remove('d')
 
print(list2)



list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
 
# looping till all 1's are removed
while (list1.count(1)):
    list1.remove(1)
     
print(list1)