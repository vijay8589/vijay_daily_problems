# Python Tuples is an immutable collection of that are more like lists. 

#  Count() Method
#The count() method of Tuple returns the number of times the given element appears in the tuple.

#Syntax:

#tuple.count(element)


# Creating tuples
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
Tuple2 = ('python', 'geek', 'python', 
          'for', 'java', 'python')
  
# count the appearance of 3
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)
  
# count the appearance of python
res = Tuple2.count('python')
print('Count of Python in Tuple2 is:', res)




 # Counting tuples and lists as elements in Tuples

 # Creating tuples
Tuple = (0, 1, (2, 3), (2, 3), 1, 
         [3, 2], 'geeks', (0))
  
# count the appearance of (2, 3)
res = Tuple.count((2, 3))
print('Count of (2, 3) in Tuple is:', res)
  
# count the appearance of [3, 2]
res = Tuple.count([3, 2])
print('Count of [3, 2] in Tuple is:', res)


