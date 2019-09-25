# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Iteratively: 
    - create while loop and flip pointers until NULL is reached 
Recursively: 
    - keep calling function and return list when NULL is reached 

Cases: 
    1. Empty list
    2. List of 1 node
    3. List of more than 1 nodes
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Case 1
        if head == None: 
            return None 
        
        # Case 2
        elif head.next == None: 
            return head 
        
        # Case 3
        prev = None
        curr = head
        
        while curr != None: 
            temp = curr.next
            curr.next = prev 
            prev, curr = curr, temp
        return prev 