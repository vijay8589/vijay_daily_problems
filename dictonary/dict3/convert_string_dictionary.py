str1 = "Jan, Feb, March"
str2 = "January | February | March"
 
# splitting first string
# in order to get keys
keys = str1.split(", ")

values = str2.split("|")
 
dictionary = {}

for i in range(len(keys)):
    dictionary[keys[i]] = values[i]
 
print(dictionary)