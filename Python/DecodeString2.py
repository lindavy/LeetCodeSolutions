
def DecodeString(input): 
	s = []
	w = []
	for char in input: 
		if char == ']': 
			# start popping
			for item in s: 
				if item.isdigit():
					
				else: 
					w.append(item) 

		else: 
			continue if char == '[' else s.append(char)


if __name__ == "__main__": 
	print("394. Decode String")
	input = "3[a]2[bc]"  # --> aaabcbc
	print("Input: ", DecodeString(input))
	input2 = "3[a2[c]]"  # --> accaccacc
	print("Input2: ", DecodeString(input2))
	input3 = "2[abc]3[cd]ef" # --> abcabccdcdcdef
	print("Input3: ", DecodeString(input3))