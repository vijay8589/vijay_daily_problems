# Input : test_str = ‘GFGaBst’ 
# Output : [‘GFG’, ‘Bst’] 
# Explanation : a is vowel and split happens on that.

# Input : test_str = ‘GFGaBstuforigeeks’ 
# Output : [‘GFG’, ‘Bst’, ‘for’, ‘geeks’] 
# Explanation : a, u, i are vowels and split happens on that.




test_str = 'GFGaBste4oCS'
 
print(test_str)
 
# splitting on vowels
vow="aeiouAEIOU"
for i in test_str:
    if i in vow:
        test_str=test_str.replace(i,"*")
res=test_str.split("*")
print(res)