# The fromkeys() method returns a dictionary with the specified keys and the specified value.


x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)


# set of vowels
keys = {'a', 'e', 'i', 'o', 'u' }

# list of number
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)

# updates the list value
value.append(2)

print(vowels)


