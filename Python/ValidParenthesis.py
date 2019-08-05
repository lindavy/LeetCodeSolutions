def isValid(s: str) -> bool:
	brackets = []
	for bracket in s: 
		if bracket == '(' or bracket == '[' or bracket == '{' or len(brackets) == 0: 
			brackets.append(bracket)
		else: 
			found = False
			for i, x in enumerate(brackets): 
				if bracket == ')' and x == '(': 
					brackets.pop(i)
					found = True
					break
				elif bracket == ']' and x == '[': 
					brackets.pop(i)
					found = True
					break
				elif bracket == '}' and x == '{': 
					brackets.pop(i)
					found = True
					break
				if found: 
			if not found: 
				brackets.append(bracket)
	return True if len(brackets) == 0 else False  

s = "{}}"
print("s: ", s)
if isValid(s): 
	print("True")
else: 
	print("False")