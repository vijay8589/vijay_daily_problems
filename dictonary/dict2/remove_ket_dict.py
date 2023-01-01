# Before remove key:   {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}

# Operation Perform:   del test_dict['Mani']

# After removing key:  {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22}

test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21}
 
# Printing dictionary before removal
print(test_dict)
 
# Using del to remove a dict
# removes Mani
del test_dict['Mani']
 
print(test_dict)
 
#del test_dict['Mani']