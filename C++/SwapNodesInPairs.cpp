/*
Problem

Input: 1 -> 2 -> 3 -> 4 -> NULL
Output: 2 -> 1 -> 4 -> 3 -> NULL

*/ 
#define NULL 0

struct ListNode {
	int val; 
	ListNode *next; 
}; 

class Solution {
public:

    ListNode* swapPairs(ListNode* head) {
    	ListNode *first, *second; 
        if (head == NULL || head->next == NULL) 
        {
        	return head; 
        }
        first = head->next; 
        second = head; 
        second->next = swapPairs(first->next); 
        first->next = second; 
        return first; 
    }
};

int main() {
	Solution s; 
	// add nodes to linked list, then run in Solution 
}