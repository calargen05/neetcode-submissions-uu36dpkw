# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node,low,high):
            if not node:
                return True
            if node.val >= high or node.val <= low:
                return False
            return helper(node.left,low,node.val) and helper(node.right,node.val,high)
            
        
        if not root.right and not root.left:
            return True
        return helper(root.left,-1001,root.val) and helper(root.right,root.val,1001)