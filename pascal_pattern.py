from math import factorial  # import the math module

n = int(input("Enter the value of n: ")) # taken the input value
for i in range(n): # print the n of rows
    for j in range(n-i+1):       
        print(end=" ")

    for j in range(i+1):

        # nCr formula     n!/(n-r)!*r! 

        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

   

print()
