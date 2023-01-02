test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
  
# printing original dictionary
print(test_dict)
  
# Remove duplicate values in dictionary
# Using loop
temp = []
res = dict()
for key, val in test_dict.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
  
# printing result 
print(res)