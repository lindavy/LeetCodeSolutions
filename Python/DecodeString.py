"""
Linda Nguyen
8/5/19

394. Decode String
	You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

	Approaches
	1. Iterate through each char and check whether it's a bracket/letter/number, then decode the string accordingly. 
	   Bad approach b/c it can get complex in input2, where there are nested brackets
	2. Use stacks to push and pop 

"""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def ReverseString(A:str)-> str: 
	s = Stack() # letters, brackets
	n = Stack() # numbers
	n_count = 0
	temp = ""
	output = "" # final string
	print("DECODE: ", A)
	for char in A: 
		s_word = ""
		if char.isdigit(): 
			n.push(int(char))
		elif char == ']': 
			while s.peek() != '[': 
				s_word += s.pop()
			print(s.pop())
			s_word = s_word[::-1] # reverse
			print("word being appended after reverse: ", s_word)

			# check if n stack is empty
			#n_count = 1 if n.isEmpty() else n_count = n.pop()
			if n.isEmpty(): 
				n_count = 1
			else: 
				n_count = n.pop()

			for i in range(0, n_count): 
				output += s_word
			# check if we have to append to letter on top of stack
			if not s.isEmpty() and s.peek().isalpha(): 
				temp = s.pop()
				temp += output
				s.push(temp)
		else: 
			s.push(char)
	return output

if __name__ == "__main__": 
	print("394. Decode String")
	input = "3[a]2[bc]"  # --> aaabcbc
	print("Input: ", ReverseString(input))
	input2 = "3[a2[c]]"  # --> accaccacc
	print("Input2: ", ReverseString(input2))
	input3 = "2[abc]3[cd]ef" # --> abcabccdcdcdef
	print("Input3: ", ReverseString(input3))
