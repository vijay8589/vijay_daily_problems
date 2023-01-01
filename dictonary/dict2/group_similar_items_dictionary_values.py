# Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 
# Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]} 
# Explanation : Similar items grouped together on occurrences. 
# Input : test_list = [7, 7, 7, 7]
# Output : {7 : [7, 7, 7, 7]}
#  Explanation : Similar items grouped together on occurrences



from collections import defaultdict
 
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
 
print(test_list)

res = defaultdict(list)
for ele in test_list:     
    res[ele].append(ele)
 
print((dict(res)))