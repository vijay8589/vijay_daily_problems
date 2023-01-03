# Python String isalnum() method checks whether all the characters in a given string 
# are either alphabet or numeric (alphanumeric) characters.

# Python String isalnum() Method Syntax:
# Syntax:  string_name.isalnum() 


string = "abc123"
print(string.isalnum())


string = "abc 123"
print(string, "is alphanumeric?", string.isalnum())
 
string = "abc_123"
print(string, "is alphanumeric?", string.isalnum())
 
string = "000"
print(string, "is alphanumeric?", string.isalnum())
 
string = "aaaa"
print(string, "is alphanumeric?", string.isalnum())