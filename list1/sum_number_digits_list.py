test_list = [12, 67, 98, 34]
 
print(test_list)
res = []
for ele in test_list:
    sum = 0
    for digit in ele:
        sum += digit
    res.append(sum)
     

print(res)