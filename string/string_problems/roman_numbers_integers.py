# Input: IX
# Output: 9
# IX is a Roman symbol which represents 9 

# Input: XL
# Output: 40
# XL is a Roman symbol which represents 40

# Input: MCMIV
# Output: 1904
# M is a thousand, 
# CM is nine hundred and 
# IV is four



# Python program to convert Roman Numerals
# to Numbers

# This function returns value of each Roman symbol


def value(r):
	if (r == 'I'):
		return 1
	if (r == 'V'):
		return 5
	if (r == 'X'):
		return 10
	if (r == 'L'):
		return 50
	if (r == 'C'):
		return 100
	if (r == 'D'):
		return 500
	if (r == 'M'):
		return 1000
	return -1


def romanToDecimal(str):
	res = 0
	i = 0

	while (i < len(str)):

		# Getting value of symbol s[i]
		s1 = value(str[i])

		if (i + 1 < len(str)):

			# Getting value of symbol s[i + 1]
			s2 = value(str[i + 1])

			# Comparing both values
			if (s1 >= s2):

				# Value of current symbol is greater
				# or equal to the next symbol
				res = res + s1
				i = i + 1
			else:

				# Value of current symbol is greater
				# or equal to the next symbol
				res = res + s2 - s1
				i = i + 2
		else:
			res = res + s1
			i = i + 1

	return res


print("Integer form of Roman Numeral is"),
print(romanToDecimal("MCMIV"))
