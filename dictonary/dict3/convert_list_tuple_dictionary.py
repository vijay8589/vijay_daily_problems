# Input : [("akash", 10), ("gaurav", 12), ("anand", 14), 
#          ("suraj", 20), ("akhil", 25), ("ashish", 30)]
# Output : {'akash': [10], 'gaurav': [12], 'anand': [14], 
#           'ashish': [30], 'akhil': [25], 'suraj': [20]}

# Input : [('A', 1), ('B', 2), ('C', 3)]
# Output : {'B': [2], 'A': [1], 'C': [3]}

# Input : [("Nakul",93), ("Shivansh",45), ("Samved",65),
#              ("Yash",88), ("Vidit",70), ("Pradeep",52)]
# Output : {'Nakul': [93], 'Shivansh': [45], 'Samved': [65], 
#             'Yash': [88], 'Vidit': [70], 'Pradeep': [52]}

# Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}



def Convert(tup, di):
    di = dict(tup)
    return di
     

tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
    ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))