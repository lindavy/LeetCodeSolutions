import unittest

class ListNode:
	def __init__(self, x:int):
		self.val = x
		self.next = None

class Solution: 
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: 
		# Pointers
		p1, p2 = l1, l2
		head = ListNode(0)
		node = head
		carry = 0
		while p1 != None or p2 != None:
			if p1 != None: 
				x = p1.val 
			else: 
				x = 0 
			
			if p2 != None: 
				y = p2.val 
			else: 
				y = 0
			
			node_sum = carry + x + y

			print(carry, '+', x, '+', y, '=', node_sum)
			carry = int(node_sum / 10)
			curr.next = ListNode(node_sum % 10)

			curr = curr.next
			if p1 != None: 			 
				p1 = p1.next	
			if p2 != None: 
				p2 = p2.next

		if carry: 
			curr.next = ListNode(carry)

		return dummyHead.next # b/c first node is 0 

class TestAddTwoNumbers(unittest.TestCase):
	'''
	Test Empty Lists
	1. one list is empty
	2. both lists are empty 
	'''
	def setUp(self): 
		pass

	def tearDown(self): 
		pass

	def list_to_array(self, head): 
		if not head: 
			return []
		arr = []
		node = head 
		
		while node: 
			arr.append(node.val)
			node = node.next
		return arr 

	def array_to_list(self, arr): 
		if not arr: 
			return None
		head = ListNode(arr[0])
		node = head 
		for i in range(1, len(arr)): 
			node.next = ListNode(arr[i])
			node = node.next 
		return head 

	def test_case1(self): 
		s = Solution()

		for i, o in [(([], []), []), 
        			(([0], [1]), [1]), 
        			(([1, 8], [0]), [1, 8]), 
        			(([2, 4, 3], [5, 6, 4]), [7, 0, 8]), 
        			(([0, 1], [9, 9, 9, 9]), [9, 0, 0, 0, 1])]:

        			head = s.addTwoNumbers(self.array_to_list(i[0]), self.array_to_list(i[1]))
        			arr = self.list_to_array(head)
        			self.assertEqual(arr, o)


if __name__ == "__main__": 
	unittest.main()
