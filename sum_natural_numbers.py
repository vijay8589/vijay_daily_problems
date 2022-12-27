# def recurSum(n):
#     if n <= 1:
#         return n
#     return n + recurSum(n - 1)
 

# n = 5
# print(recurSum(n))




n = 5
total_sum = 0
for i in range(1, n+1):
    total_sum = total_sum + i
print("Total sum is:", total_sum)
if total_sum%2 == 0:
    print("even numbers")
else:
    print("odd numbers")
