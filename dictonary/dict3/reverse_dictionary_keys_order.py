from collections import OrderedDict
  
test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5} 
res = OrderedDict(reversed(list(test_dict.items())))
print(res)



  
# initializing dictionary
test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}
  
# printing original dictionary
print("The original dictionary : " + str(test_dict))
  
# Reverse Dictionary Keys Order
# Using reversed() + items()
res = dict(reversed(list(test_dict.items())))
 
print(res)