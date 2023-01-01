# Input : test_list = [“Gfg”, “is”, “Best”], subs_dict = {“Gfg” : [5, 6, 7], “is” : [7, 4, 2]}, K = 0 
# Output : [5, 7, “Best”] 
# Explanation : “Gfg” and “is” is replaced by 5, 7 as 0th index in dictionary value list.
# Input : test_list = [“Gfg”, “is”, “Best”], subs_dict = {“Gfg” : [5, 6, 7], “Best” : [7, 4, 2]}, K = 0
# Output : [5, “is”, 7] 
# Explanation : “Gfg” and “Best” is replaced by 5, 7 as 0th index in dictionary value list.

test_list = ["Gfg", "is", "Best"]
print(test_list)
subs_dict = {
    "Gfg" : [5, 6, 7],
    "is" : [7, 4, 2],
}
 
K = 2
 
res = [ele if ele not in subs_dict else subs_dict[ele][K]
                                     for ele in test_list]
         
print(res)