x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


str1 = 'GeeksforGeeks'
 
# lambda returns a function object
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))

#  Lambda Function with List Comprehension
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
 
for item in is_even_list:
    print(item())


#  Lambda Function with if-else


# Example of lambda function using if-else
Max = lambda a, b : a if(a > b) else b
 
print(Max(1, 2))




# multiple statements
List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
 
# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)
 
# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
 
print(res)




#  Find the maximum element in a list using lambda and reduce() function



import functools
 
lis = [1, 3, 5, 6, 2, ]
 
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))