# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        nodes = []

        def helper(node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            nodes.append(node.val)
        
        helper(root)

        return nodes