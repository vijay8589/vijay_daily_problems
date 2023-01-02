test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
res = []
for key, val in test_dict.items():
    res.append([key] + val)
 
print(res)