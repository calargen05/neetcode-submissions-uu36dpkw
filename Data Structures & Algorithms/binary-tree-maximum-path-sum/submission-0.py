# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = float('-inf')

        def dfs(node):
            nonlocal global_max

            if not node:
                return 0
            
            left_path = max(0, dfs(node.left))
            right_path = max(0, dfs(node.right))

            curr_sum = node.val + left_path + right_path
            
            global_max = max(global_max, curr_sum)

            return node.val + max(left_path, right_path)
        
        dfs(root)

        return global_max