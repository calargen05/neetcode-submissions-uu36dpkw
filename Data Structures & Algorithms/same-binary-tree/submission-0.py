# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1,stack2 = deque(),deque()

        stack1.appendleft(p)
        stack2.appendleft(q)

        while stack1 and stack2:
            node1,node2 = stack1.popleft(),stack2.popleft()
            if not node1:
                if node2:
                    return False
            if not node2:
                if node1:
                    return False
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                if node1.left:
                    stack1.appendleft(node1.left)
                else:
                    stack1.appendleft(None)
                if node1.right:
                    stack1.appendleft(node1.right)
                else:
                    stack1.appendleft(None)
                if node2.left:
                    stack2.appendleft(node2.left)
                else:
                    stack2.appendleft(None)
                if node2.right:
                    stack2.appendleft(node2.right)
                else:
                    stack2.appendleft(None)
        
        if stack1 or stack2:
            return False
        
        return True