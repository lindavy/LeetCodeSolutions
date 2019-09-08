class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: 
            return head 
        first = head.next
        second = head
        second.next = self.swapPairs(first.next)
        first.next = second
        return first 