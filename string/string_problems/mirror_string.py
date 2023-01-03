test_str = 'void'
 
# printing original string
print(test_str)
 
mir_dict = {'b':'d', 'd':'b', 'i':'i', 'o':'o', 'v':'v', 'w':'w', 'x':'x'}
res = ''
 
# accessing letters from dictionary
for ele in test_str:
    if ele in mir_dict:
        res += mir_dict[ele]
     
    else:
        res = "Not Possible"
        break
 
print("The mirror string : " + str(res))