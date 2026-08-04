# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue, levels = deque(), []
        queue.append(root)

        while queue:
            sublist = []
            for i in range(len(queue)):
                node = queue.popleft()
                sublist.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(sublist)
        
        right_side = []

        for arr in levels:
            right_side.append(arr[len(arr)-1].val)
        
        return right_side