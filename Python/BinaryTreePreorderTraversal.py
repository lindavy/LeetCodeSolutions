"""
Given a binary tree, return it's values using preorder traversal 

Approach: Recursion 
	Base case - when node returns is NULL 
"""

# SOLUTION 1
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        preorderList = [] 
        
        # Case 1: tree is empty
        if root is None: 
            return preorderList
        
        # Case 2: tree exists 
        treeStack = []
        treeStack.append(root)
        
        while len(treeStack) > 0: 
            node = treeStack.pop()
            preorderList.append(node.val)
            if node.right != None: 
                treeStack.append(node.right)
            if node.left != None: 
                treeStack.append(node.left)
        return preorderList

 # SOLUTION 2
 class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(node: TreeNode, preorderList: List[int]) -> List[int]:
            if node is None: 
                return 
            preorderList.append(node.val)
            helper(node.left, preorderList)
            helper(node.right, preorderList)
            return preorderList
        preorderList = [] 
        return helper(root, preorderList)
         
            
        
        
        
        
        
        