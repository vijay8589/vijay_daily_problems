# Input: list = [4, 5, 6, 7, 8, 9]
# Output : [9, 8, 7, 6, 5, 4] 


lst = [4, 5, 6, 7, 8, 9]
lst.reverse()
print(lst)


def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst
 
lst = [4, 5, 6, 7, 8, 9]
print(Reverse(lst))