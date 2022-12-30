test_list = [5, 6, [], 3, [], [], 9]

res = [ele for ele in test_list if ele != []]
 
print(res)

# using filter method

test_list = [5, 6, [], 3, [], [], 9]

res = list(filter(None, test_list))
 
print(res)