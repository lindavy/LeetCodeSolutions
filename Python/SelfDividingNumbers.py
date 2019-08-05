from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    	output = []
    	 
    	for x in range(left, right): 
    		goodVal = True
    		for y in str(x): 
    			# 2 fail cases (1. cannot mod by 0 and 2. if value does not mod evenly)
    			if int(y) == 0 or x % int(y) > 0:  # if a single digit fails, then break loop
    				goodVal = False
    				break
    		if goodVal: 
    			output.append(x)
    	print("Output: ", output)
    	return output
        
print("728. Self Dividing Numbers\n")
s = Solution()
left = 1
right = 22
s.selfDividingNumbers(left, right + 1)
