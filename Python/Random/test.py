def bitwiseComplement(n):
	# converting the int to a string we can loop over. The [ 2 : ] turns a string like "0b1010" to "1010"
	binaryString = str(bin(n))[2:]
	
	# converting the binary string to a list we can change
	binaryString = [ char for char in binaryString ]
	
	# flipping the bits of the binary string
	for i in range(len(binaryString)):
		if binaryString[i] == '1':
			binaryString[i] = '0'
		else:
			binaryString[i] = '1'
	
	# converting the list back into a string
	binaryString = ''.join(binaryString)
	
	# converting the string back into an int, since the string is binary, we need to specify base-2
	result = int(binaryString, 2)
	
	return result

print(bitwiseComplement(10))