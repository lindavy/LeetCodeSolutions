def OnesComplement(N: int): 
	binaryresult = []
	decimalresult = 0
	q = N

	# Convert to binary and apply one's complement
	while True:
		if q == 0:
			print("Quotient is zero!")
			break
		q, r = divmod(q, 2)
		print("Quotient: ", q, " Remainder: ", r)
		binaryresult.append(0) if r else binaryresult.append(1)	
	print ("1's Binary: ", binaryresult)

	# Get decimal value
	for bitpos, bit in enumerate(binaryresult): 
		if bit:  # if bit is '1' 
			decimalresult += 2 ** bitpos
	print("Decimal: ", decimalresult)
OnesComplement(78)

