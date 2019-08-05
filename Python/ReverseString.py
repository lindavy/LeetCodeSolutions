"""
Linda Nguyen
Date: 8/5/19

344. Reverse String
	Modify string in place with O(1) extra memory
"""
def ReverseString(A:int): 
	left = 0
	right = len(A) - 1
	while left < right: 
		A[left], A[right] = A[right], A[left]
		left += 1
		right -= 1
	return A

if __name__ == "__main__": 
	print("344. Reverse String\n")
	input = ['h', 'e', 'l', 'l', 'o']
	print("String: ", input)
	print("Reversed: ", ReverseString(input), '\n')

	input = ['e', 'v', 'e', 'r', 'y', 'o', 'n', 'e']
	print("String: ", input)
	print("Reversed: ", ReverseString(input))
