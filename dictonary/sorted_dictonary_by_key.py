"""Input:
key_value['ravi'] = '10'       
key_value['rajnish'] = '9'
key_value['sanjeev'] = '15'
key_value['yash'] = '2'
key_value'suraj'] = '32'

Output:
[('rajnish', '9'), ('ravi', '10'), ('sanjeev', '15'), ('suraj', '32'), ('yash', '2')]"""

from collections import OrderedDict
dict = {'ravi': '10', 'rajnish': '9',
        'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)