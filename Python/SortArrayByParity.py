from typing import List 

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        print("A: ", A)

        unsorted = True

        counter = len(A) - 1

        for i in range(0, len(A)): 

        	if A[i] % 2 == 0: 
        		temp = A[i]
        		A[i] = A[counter]
        		A[counter] = temp
        		counter -= 1
        		print("A: ", A)
        	if counter == i: 
        		break; 
        	
        return A



s = Solution()
intlist = [3, 1, 2, 4, 6, 7, 9, 10, 11]  # expect: [4, 2, 3, 1] or [2, 4, 3, 1]
print("Sorted Array: ", s.sortArrayByParity(intlist))

# Odd - Even 
# Slowest: linear check (pop and push even numbers till you reach end of list)
# Faster: odd-left and even-right pointers (con: more memory, but faster) -- recursively
# 3 1 2 4 6 7 9 -> 3 1 9 4 6 7 2 -> 3 1 9 7 6 4 2 ta-dah