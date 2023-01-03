import re

# 'a', 'b', 'c', 'd', 'e'.
p = re.compile('[a-e]')
 
# findall() searches for the Regular Expression
# and return a list upon finding
print(p.findall("Aye, said Mr. Gibenson Stark"))