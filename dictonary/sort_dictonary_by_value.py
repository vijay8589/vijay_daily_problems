"""Input:
key_value['ravi'] = 10       
key_value['rajnish'] = 9
key_value['sanjeev'] = 15
key_value['yash'] = 2
key_value'suraj'] = 32

Output:
{'ravi': 2, 'rajnish': 9, 'sanjeev': 10, 'yash': 15, 'suraj': 32}"""

# Creates a sorted dictionary (sorted by key)

from collections import OrderedDict
import numpy as np
 
dict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(dict)
 
keys = list(dict.keys())
values = list(dict.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
 
print(sorted_dict)