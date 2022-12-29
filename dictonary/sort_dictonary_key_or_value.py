"""Input:
key_value[2] = '56'       
key_value[1] = '2'
key_value[4] = '12'
key_value[5] = '24'
key_value[6] = '18'
key_value[3] = '323'

Output:
1 2 3 4 5 6 """

def dictionairy():
    key_value = {}
 
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
 
     
    print("key_value", key_value)
 

    # dictionary’s keys.
    for i in sorted(key_value.keys()):
        print(i, end=" ")
 
 
def main():
    dictionairy()
 
if __name__ == "__main__":
    main()




# Sorting the Keys and Values in Alphabetical Order using the Key

# Input:
# key_value[2] = '56'       
# key_value[1] = '2'
# key_value[4] = '12'
# key_value[5] = '24'
# key_value[6] = '18'
# key_value[3] = '323'

# Output:
# (1, 2) (2, 56) (3, 323) (4, 24) (5, 12) (6, 18) 

def dictionairy():
    key_value = {}
    
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
     
    print("key_value",key_value)
    print(sorted(key_value.items(), key=lambda kv:
                 (kv[1], kv[0])))
 
 
def main():
    dictionairy()
 
if __name__ == "__main__":
    main()