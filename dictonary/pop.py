# removes and returns the specified element from the dictionary.
test_dict = {"Nikhil": 7, "Akshat": 1, "Akash": 2}
 
# Printing initial dict
print("The dictionary before deletion : " + str(test_dict))
 
# using pop to return and remove key-value pair.
pop_ele = test_dict.pop('Akash')
print("Value associated to popped key is : " + str(pop_ele))
 
 
