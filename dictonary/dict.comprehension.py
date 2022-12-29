# Dictionary Comprehension

square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)


"""Multiple if Conditional Dictionary Comprehension"""

original_dict = {'vijay': 38, 'kumar': 48, 'raju': 57, 'vicky': 33}

new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)



"""if-else Conditional Dictionary Comprehension"""

original_dict = {'vijay': 38, 'kumar': 48, 'raju': 57, 'vicky': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young')
    for (k, v) in original_dict.items()}
print(new_dict_1)




dictionary = dict()
for k1 in range(11, 16):
    dictionary[k1] = dict()
    for k2 in range(1, 6):
        dictionary[k1][k2] = k1*k2
print(dictionary)