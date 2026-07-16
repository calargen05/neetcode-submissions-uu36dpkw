# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False

            return helper(node1.left, node2.left) and helper(node1.right, node2.right)
        
        # find the subroot
        queue = deque()
        queue.append(root)
        node = None
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                isSub = helper(node,subRoot)
                if isSub:
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False
        