"""
Cases 
	(1) Negative values -> FALSE
	(2) Value ends in zero, meaning the first digit should also be 0 -> FALSE usually
	(3) Value is 0 -> TRUE
	(4) Positive values 

Approach
	Reverse the later half of the values and compare it to the first half
"""
def isPalindrome(x:int) -> bool: 
	if x < 0 or (x % 10 == 0 and x != 0): 
		return False
	elif x == 0: 
		return True
	else: 
		rx = 0 
		while x > rx:
			rx = (x % 10) + (rx * 10)  # multipling by 10 shifts value one digit to the left 
			x = int(x / 10)  # get rid of last digit
		return x == rx or x == int(rx / 10)  # divide by 10 in case number of digits is odd
		"""
		Odd digit example: 
		Input: 12321
		x = 12
		rx = 123 / 10 = 12
		Now you can compare x and rx!
		* The reverse of center value is still the same position, so you can toss it 
		"""


if __name__ == "__main__": 
	while True: 
		print("Enter a value: ", end = '')
		#v = int(input())
		print("PALINDROME") if isPalindrome(int(input())) else print("NOT A PALINDROME")