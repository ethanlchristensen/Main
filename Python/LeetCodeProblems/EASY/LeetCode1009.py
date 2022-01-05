# LEET CODE 1009 Complement of Base 10 Integer
# Given a Base-10 Integer, return the complenent of this Integer
# Note: the complement of an integer is the integer you get when 
# you flip all the 0's to 1's and all the 1's to 0's in its binary
# representation . . . For example . . .
# 5 -> 101 -> 010 -> 2
# 10 -> 1010 -> 0101 -> 5

def bitwiseComplementOneLiner(n):
    return int((''.join(['1' if str(bin(n))[2:][i] == '0' else '0' for i in range(len(str(bin(n))[2:]))])), 2)

def bitwiseComplementExpanded(n):
    # converting the int to a string we can loop over. The [ 2 : ] turns a string like "0b1010" to "1010"
	binaryString = str(bin(n))[2:]
	
	# converting the binary string to a list we can change
	binaryString = [ char for char in binaryString ]
	
	# flipping the bits of the binary string
	for i in range(len(binaryString)):
		if binaryString[i] == '0':
			binaryString[i] = '1'
		else:
			binaryString[i] = '0'
	
	# converting the list back into a string
	binaryString = ''.join(binaryString)
	
	# converting the string back into an int, since the string is binary, we need to specify base-2
	result = int(binaryString, 2)
	
	return result

test_cases = [10, 20, 5, 12, 89, 63, 14]
for case in test_cases:
    print("ONE LINER: {}".format(bitwiseComplementOneLiner(case)))
    print("EXPANDED: {}".format(bitwiseComplementExpanded(case)))