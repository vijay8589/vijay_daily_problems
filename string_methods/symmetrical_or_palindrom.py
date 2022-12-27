"""To print the gievn string upercase to lowercase"""

# using the in build function.

v ="VIJAY IS A SOFTWARE ENGINEER"
print(v.casefold())  # casefold method use to convert upercase to lowercase


# with out using in build function
# find palindrome or not

#string = "khokho"
string = "amaama"
if (string==string[::-1]):
    print("is palindrom")
else:
    print("is not palindrom")

#Find symetrical or not
a = len(string)
b = 0
if a%2:
    mid = a//2+1
else:
    mid= a//2
start=0
end= mid
while(start <mid and end<a):
    if(string[start]== string[end]):
        start= start+1
        end= end+1
    else:
        b=1
        break
if b==0:
    print("symmetrical")
else:
    print("not symmetrical")





#string = "khokho"
r = ""
for i in string:
    r = i + r
#print("reversed string:", r)
if (string==r):
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")


