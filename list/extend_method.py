# extend method
l = [1, 2, 3]
l.extend([4, 5, 6])
print(l)

# slicing

l = [1, 2, 3]
l[:0] = [4]
print(l)

l[:-1:] = [5]
print(l)


# chain metod used
from itertools import * 

l = [1, 2, 3]
print(list(chain(l, [6, 7, 8])))