# Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]
# Explanation : Values mapped by custom key, “name” -> “Gfg”, “id” -> 3.

# Input : test_list = [“Gfg”, 10], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 10}]
# Explanation : Conversion of lists to list of records by keys mapping.

test_list = ["vijay", 3, "is", 8, "Best", 10, "for", 18, "vijay", 33]
   
key_list = ["name", "number"]
  
n = len(test_list)
res = []
for idx in range(0, n, 2):
    res.append({key_list[0]: test_list[idx], key_list[1] : test_list[idx + 1]})
   
print(res)