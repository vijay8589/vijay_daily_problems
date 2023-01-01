# Input : str = geeksforgeeks, k = 3
# Output : r
# First non-repeating character is f,
# second is o and third is r.

# Input : str = geeksforgeeks, k = 2
# Output : o

# Input : str = geeksforgeeks, k = 4
# Output : Less than k non-repeating
#          characters in input.

from collections import OrderedDict
 
def kthRepeating(input,k):
    dict=OrderedDict.fromkeys(input,0)
    for ch in input:
        dict[ch]+=1
 
    nonRepeatDict = [key for (key,value) in dict.items() if value==1]
     
    # now return (k-1)th character from above list
    if len(nonRepeatDict) < k:
        return 'Less than k non-repeating characters in input.'
    else:
        return nonRepeatDict[k-1]

if __name__ == "__main__":
    input = "geeksforgeeks"
    k = 3
    print (kthRepeating(input, k))