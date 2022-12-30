# Input: 
# string = "engineers rock"
# pattern = "er";
# Output: true
# Explanation: 
# All 'e' in the input string are before all 'r'.


# Input: 
# string = "engineers rock"
# pattern = "gsr";
# Output: false
# Explanation:
# There are one 'r' before 's' in the input string.

from collections import OrderedDict 
  
def checkOrder(input, pattern): 
      
    dict = OrderedDict.fromkeys(input) 
  
    ptrlen = 0
    for key,value in dict.items(): 
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
          
        if (ptrlen == (len(pattern))): 
            return 'true'
  
    return 'false'
  
if __name__ == "__main__": 
    input = 'engineers rock'
    pattern = 'er'
    print (checkOrder(input,pattern)) 