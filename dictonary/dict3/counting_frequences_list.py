# Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
#                   4, 4, 4, 2, 2, 2, 2]
# Output : 1 : 5
#          2 : 4
#          3 : 3
#          4 : 3
#          5 : 2
# Explanation : Here 1 occurs 5 times, 2 
#               occurs 4 times and so on...



def CountFrequency(my_list):

	# Creating an empty dictionary
	freq = {}
	for item in my_list:
		if (item in freq):
			freq[item] += 1
		else:
			freq[item] = 1

	for key, value in freq.items():
		print ("% d : % d"%(key, value))


if __name__ == "__main__":
	my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

	CountFrequency(my_list)
