numbers = [1, 3, 4, 2]
# Sorting list of Integers in ascending
print(numbers.sort())  
print(numbers)           # [1, 2, 3, 4]

 
# sorting numbers in descending Order
# Creating List of Numbers
numbers = [1, 3, 4, 2]
 
# Sorting list of Integers in descending
numbers.sort(reverse = True)

# without using sort method
my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
new_list = []

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print(new_list)