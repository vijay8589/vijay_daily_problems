# Input : test_dict = {‘Gfg’ : 4, ‘best’ : 9}, test_list = [8, 2]
# Output : {8: {‘Gfg’: 4}, 2: {‘best’: 9}}
# Explanation : Index-wise key-value pairing from list [8] to dict {‘Gfg’ : 4} and so on.

# Input : test_dict = {‘Gfg’ : 4}, test_list = [8]
# Output : {8: {‘Gfg’: 4}}
# Explanation : Index-wise key-value pairing from list [8] to dict {‘Gfg’ : 4}.


test_dict = {'Gfg' : 4, 'is' : 5, 'best' : 9} 
test_list = [8, 3, 2]
res = {}
for key, ele in zip(test_list, test_dict.items()):
    res[key] = dict([ele])
 
print(res)