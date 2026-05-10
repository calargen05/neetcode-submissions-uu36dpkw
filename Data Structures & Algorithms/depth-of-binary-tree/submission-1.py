# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0
        
        levels = set()

        def dfs(node, level):
            if not node.left and not node.right:
                levels.add(level)
                return
            if node.left:
                dfs(node.left,level+1)
            if node.right:
                dfs(node.right,level+1)
        
        dfs(root,1)

        return max(levels)