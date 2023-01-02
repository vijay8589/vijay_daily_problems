# Input : 
# test_dict = {1 : ‘Gfg is best for geeks’} 
# sub_list = [‘love’, ‘good’] ( Strings to check in values ) 
# Output : {1: ‘Gfg is best for geeks’}
# Input : 
# test_dict = {1 : ‘Gfg is love’, 2: ‘Gfg is good’} 
# sub_list = [‘love’, ‘good’] ( Strings to check in values ) 
# Output : {} 
 

 
# Python3 code to demonstrate working of
# Remove keys with substring values
# Using any() + generator expression

# initializing dictionary
test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}
sub_list = ['love', 'good']

res = dict()
for key, val in test_dict.items():
    if not any(ele in val for ele in sub_list):
	    res[key] = val
		
print(res)
