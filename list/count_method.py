# count method
list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b']
print(list2.count('b'))


# index method

# Python index() is an inbuilt function in Python, which searches for a given element from the 
# start of the list and returns the index of the first occurrence.


list2 = ['cat', 'bat', 'mat', 'cat', 'pet']
 
# Will print the index of 'bat' in list2
print(list2.index('bat'))



# list of items
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
 
# Will print index of '4' in sublist
# having index from 4 to 8.
print(list1.index(4, 4, 8))


# list of items
list1 = [6, 8, 5, 6, 1, 2]
 
# Will print index of '6' in sublist
# having index from 1 to end of the list.
print(list1.index(6, 1))



# insert method

  
# before any element using insert() method 
  
list1 = [ 1, 2, 3, 4, 5, 6 ]
  
# Element to be inserted 
element = 13 
  
# Element to be inserted before 3
beforeElement = 3 
  
# Find index
index = list1.index(beforeElement) 
  
# Insert element at beforeElement 
list1.insert(index, element) 
print(list1)