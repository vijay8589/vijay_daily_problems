#The capitalize() method returns a string where the first character is upper case, and the rest is lower case

txt = "hello, and welcome to my world."

x = txt.capitalize()
print(x)

# Using string slicing() and upper() method

txt = "hello, and welcome to my world."
result = txt[0].upper() + txt[1:]
print(result)


# 2. casefold

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

