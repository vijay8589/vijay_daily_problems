# Input: s = “geeks quiz practice code” 
# Output: s = “code practice quiz geeks”

# Input: s = “i love programming very much” 
# Output: s = “much very programming love i” 


s = "geeks quiz practice code"
s1 = s.split()[::-1]
print(" ".join(s1))


s = "i love programming very much"
words = s.split(' ')
string = []
for word in words:
    string.insert(0, word)
 
 
print(" ".join(string))