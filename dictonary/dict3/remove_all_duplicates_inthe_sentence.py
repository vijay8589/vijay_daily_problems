# Input : Geeks for Geeks
# Output : Geeks for

# Input : Python is great and Java is also great
# Output : is also Java Python and great


s = "Python is great and Java is also great"
l = s.split()
k = []
for i in l:
    if (s.count(i)>=1 and (i not in k)):
        k.append(i)
print(' '.join(k))



 
string = 'Python is great and Java is also great'
 
print(' '.join(dict.fromkeys(string.split())))